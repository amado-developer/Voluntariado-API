from project_request.models import ProjectRequest
from project_application.models import ProjectApplication
from project_request.serializers import ProjectRequestSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django_pandas.io import read_frame
import pandas as pd

from multi_rake import Rake
from rest_framework import viewsets
from majors.models import Major
from faculties.models import Faculty
from users.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.core.mail import send_mail
from nltk.tokenize import word_tokenize
from gensim.corpora.dictionary import Dictionary
from gensim.models import TfidfModel
from gensim.similarities import MatrixSimilarity

def get_keywords(text):
        text = (
            text
        )
        rake = Rake(
            min_chars=3,
            max_words=1,
            min_freq=1,
            language_code='es',
            stopwords=None,
            lang_detect_threshold=100,
            max_words_unknown_lang=10,
            generated_stopwords_percentile=80,
            generated_stopwords_max_len=10,
            generated_stopwords_min_freq=2,
            )

        keywords = rake.apply(
            text,
            text_for_stopwords=None,
        )
        return keywords
def no_commas(doc):
    no_commas = [t for t in doc if t != ',']

    return no_commas

def keywords_recommendation(all_projects, keywords, number_of_hits, data):
    query_doc_bow = data[0].doc2bow(keywords)
    query_doc_tfidf = data[1][query_doc_bow]
    similarity_array = data[2][query_doc_tfidf]
    similarity_series = pd.Series(similarity_array.tolist(), index=all_projects.index)
    top_hits = similarity_series.sort_values(ascending=False)[:number_of_hits]
    top = top_hits.index.tolist()
    top_3 = []
    for id, (score) in enumerate(zip(top_hits.index, top_hits)):
        if(score[1] > 0.3):
            top_3.append(top[id])
    return top_3

class ProjectRequestViewSet(viewsets.ModelViewSet):
    serializer_class= ProjectRequestSerializer
    queryset = ProjectRequest.objects.all()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='post-request')
    def post_request(self, request):
        project_request_querydict = request.data
        project_request_dict = dict(project_request_querydict)
        faculty_object = Faculty.objects.get(faculty=project_request_dict['faculty'])
        major_object = Major.objects.get(major=project_request_dict['major'], faculty=faculty_object)
        project_request = ProjectRequest()
        project_request.company_name = project_request_dict['company_name']
        project_request.project_name = project_request_dict['project_name']
        project_request.description = project_request_dict['description']
        project_request.requirements = project_request_dict['requirements']
        project_request.phone_number = project_request_dict['phone_number']
        project_request.email_address = project_request_dict['email_address']
        project_request.company_address = project_request_dict['company_address']
        project_request.about_us = project_request_dict['about_us']
        project_request.major = major_object
        project_request.tags = project_request_dict['tags']
        project_request.save()
        return Response({})

    @action(detail=False, methods=['get'], url_path='pending-requests', permission_classes=[AllowAny])
    def pending_requests(self, request):
        requests = ProjectRequest.objects.filter(is_approved=False)
        return Response(ProjectRequestSerializer(requests, many=True).data)

    @action(detail=False, methods=['get'], url_path='available-projects', permission_classes=[AllowAny])
    def available_projects(self, request):
        student_id = request.query_params['student_id']
        project_applications = ProjectApplication.objects.filter(student_id=student_id)
        requests = ProjectRequest.objects.filter(is_approved=True)

        filtered_requests = []
        for request in requests:
            filtered_requests.append(request)

        for request in requests:
            for project_application in project_applications:
                if(request.id == project_application.project_id):
                    filtered_requests.remove(request)

        print(filtered_requests)
        return Response(ProjectRequestSerializer(filtered_requests, many=True).data)
  

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-request-email')
    def send_request_email(self, request):
        major = request.data['major']   
        project_request = ProjectRequest.objects.last()
        request_major = project_request.major
        principal = User.objects.get(major=request_major, is_staff=True)
        principal_firstname = principal.first_name
        principal_lastname = principal.last_name
        principal_email = principal.email
        company = request.data['company']
        project_name = request.data['projectName']
        subject = 'Solicitud de Nuevo Proyecto - Horas de Extensión'
        message = '''Estimado {} {}, la organización {} ha enviado una solicitud para el proyecto de horas de extensión "{}".
        '''.format(principal_firstname, principal_lastname, company, project_name)
        sender = 'horasdeextensionuvg@gmail.com'
        fail_silently=False
        result = send_mail(subject, message, sender, [principal_email], fail_silently)
        return Response(result)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-notification-email')
    def send_notification_email(self, request):
        email = request.data['email']
        company = request.data['company']
        project = request.data['projectName']
        project_request = ProjectRequest.objects.last()
        subject = 'Universidad del Valle de Guatemala - Solicitud creada con éxito'
        message = ''' Estimados {}, su solicitud del proyecto "{}" ha sido enviada correctamente, nos estaremos comunicando con ustedes. '''.format(company, project)
        sender = 'horasdeextensionuvg@gmail.com'
        fail_silently=False
        result = send_mail(subject, message, sender, [email], fail_silently)
        return Response(result)
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='send-confirmation-email')
    def send_confirmation_email(self, request):
        email = request.data['email']
        company = request.data['company']
        project = request.data['project']
        isApproved = request.data['isApproved']
        subject = 'Universidad del Valle de Guatemala - Solicitud de proyecto'
        message = ''
        sender = 'horasdeextensionuvg@gmail.com'
        fail_silently=False
        print(type(isApproved))
        if isApproved == True:
            message = ''' Estimados {}, su solicitud del proyecto "{}" ha sido aprobada, puede ingresar con su usuario para llevar el seguimiento del proyecto.'''.format(company, project)
        else:
            message = ''' Estimados {}, su solicitud del proyecto "{}" no ha sido aprobada'''.format(company, project)
        result = send_mail(subject, message, sender, [email], fail_silently)
        return Response({})

    @action(detail=False, methods=['get'], permission_classes=[AllowAny], url_path='recommended-projects')
    def recomended_projects(self, request):
        projects = ProjectRequest.objects.all()
        project_keywords_dict = {}
        projects_dict = {}
        tags_list = []
        for project in projects:
            description = project.description
            description_keywords = get_keywords(description.replace('"', ''))
            tags = project.tags.replace('  ', ',').lower() 
            for keyword in description_keywords:
                tags += ',' + keyword[0].lower()
            tags_list.append(tags)
        df = read_frame(projects, fieldnames=['id', 'tags'], index_col=['id'])
        df['tags'] = tags_list
        keywords = df['tags'].tolist()
        keywords = [word_tokenize(keyword.lower()) for keyword in keywords]
        keywords = [no_commas(kw) for kw in keywords]
        processed_keywords = keywords
        dictionary = Dictionary(processed_keywords)
        corpus = [dictionary.doc2bow(doc) for doc in processed_keywords]
        tfidf = TfidfModel(corpus)
        sims = MatrixSimilarity(tfidf[corpus], num_features=len(dictionary))
        top_3 = keywords_recommendation(all_projects=df, keywords=['uvg', 'gasolina', 'potente', 'mcdonald', 'mecanico', 'gg', 'carros'], number_of_hits=3, data=[dictionary, tfidf, sims])
        projects = []
        for id in top_3:
            projects.append(ProjectRequestSerializer(ProjectRequest.objects.get(pk=id)).data)
        return Response(projects)

