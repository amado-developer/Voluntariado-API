import django
from django_pandas.io import read_frame
import numpy as np
import nltk
from multi_rake import Rake
from gensim.models import TfidfModel
from gensim.similarities import MatrixSimilarity
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
from project_request.models import ProjectRequest
from gensim.corpora.dictionary import Dictionary

class ProjectRecommendation(object):
    def __init__(self, projects):
        self.projects = projects
        self.project_keywords_dict = {}
        self.projects_dict = {}

    def project_keywords(self):
        tags_list = []
        for project in self.projects:
            description = project.description
            description_keywords = self.get_keywords(description)
            print(description_keywords)
            tags = project.tags.replace('  ', ',') 
            tags_list.append(tags) 
        return tags_list

    

projects = ProjectRequest.objects.all()
pr = ProjectRecommendation(projects)

tags = pr.project_keywords()
df = read_frame(projects, fieldnames=['id', 'tags'], index_col=['id'])
df['tags'] = tags














