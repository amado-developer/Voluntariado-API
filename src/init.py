from faculties.models import Faculty
from majors.models import Major
from users.models import User
from project_request.models import ProjectRequest
from project_request_images.models import ProjectRequestImages
from project_request_links.models import ProjectRequestLinks
from django.core.files import File

#TO RUN THIS FILE USE python manage.py shell < init.py

'''
Faculties
'''
engineering = Faculty(faculty="Ingeniería")
engineering.save()

education = Faculty(faculty='Educación')
education.save()

humanistics = Faculty(faculty='Ciencias y Humanidades')
humanistics.save()

socials = Faculty(faculty='Ciencias Sociales')
socials.save()

design = Faculty(faculty='Design Innovation & Arts Shool')
design.save()

business = Faculty(faculty='Business and Management School')
business.save()
'''
----------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Engineering Faculty Majors
'''

biomedical = Major(major='Biomédica', faculty=engineering)
biomedical.save()

biotec = Major(major='Biotecnología Industrial',faculty= engineering)
biotec.save()

food = Major(major='Ciencias de Alimentos', faculty=engineering)
food.save()

admin_science = Major(major='Ciencia de la Administración', faculty=engineering)
admin_science.save()

data_science = Major(major='Ciencia de los datos', faculty=engineering)
data_science.save()

civil = Major(major='Civil', faculty=engineering)
civil.save()

amb_civil = Major(major='Civil Ambiental', faculty=engineering)
amb_civil.save()

arq_civil = Major(major='Civil Arquitectónica', faculty=engineering)
arq_civil.save()

ind_civil = Major(major='Civil Industrial', faculty=engineering)
ind_civil.save()

computer_science = Major(
    major='Ciencias de la computación y tecnologías de la información'
    ,faculty=engineering)

computer_science.save()

electronics = Major(major='Electrónica', faculty=engineering)
electronics.save()

industrial = Major(major='Ingeniería Industrial', faculty=engineering)
industrial.save()

mechanics = Major(major='Mecánica', faculty=engineering)
mechanics.save()

ind_mechanics = Major(major='Mecánica Industrial', faculty=engineering)
ind_mechanics.save()

mechatronics = Major(major='Mecatrónica', faculty=engineering)
mechanics.save()

chemistry = Major(major='Química', faculty=engineering)
chemistry.save()

ind_chemistry = Major(major='Química Industrial', faculty=engineering)
chemistry.save()
'''
----------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Education Majors
'''

prof_edu = Major(major = 'Licenciatura en Educación', faculty=education)
prof_edu.save()

prof_science = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Ciencias Biológica y Químicas', faculty=education)
prof_science.save()

prof_socials = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Ciencias Sociales.', faculty=education)
prof_socials.save()

prof_communication = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Comunicación y Lenguaje.', faculty=education)
prof_communication.save()

prof_inclusive = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Educación Inclusiva.', faculty=education)
prof_inclusive.save()

prof_music = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Educación Musical.', faculty=education)
prof_music.save()

prof_elementary =  Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Educación Primaria.', faculty=education)
prof_elementary.save()

prof_english = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en English Language Teaching.', faculty=education)
prof_english.save()

prof_maths = Major(major = 'Profesorado y Licenciatura en Educación con Especialidad en Matemática y Ciencias Físicas.', faculty=education)
prof_maths.save()

'''
----------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Humanistics Majors
'''
bioqui = Major(major='Bioquímica y Microbiología', faculty=humanistics)
bioqui.save()

biotech = Major(major='Biotecnología Molecular', faculty=humanistics)
biotech.save()

leters = Major(major='Comunicación y Letras', faculty=humanistics)
leters.save()

physics = Major(major='Física', faculty=humanistics)
physics.save()

math = Major(major='Matemática Aplicada', faculty=humanistics)
math.save()

nutri = Major(major='Nutrición', faculty=humanistics)
nutri.save()

chemistry = Major(major='Química', faculty=humanistics)
chemistry.save()

farmChemistry = Major(major='Química Farmacéutica', faculty=humanistics)
farmChemistry.save()

'''
---------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Social Sciences Majors
'''
antropology = Major(major='Antropología y Sociología', faculty=socials)
antropology.save()

arqueology = Major(major='Arqueología', faculty=socials)
arqueology.save()

psicology = Major(major='Psicología', faculty=socials)
psicology.save()

internation_rel = Major(major='Relaciones Internacionales & Master of Artes in Global Affairs'
,faculty=socials)
internation_rel.save()
'''
----------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Design Innovation & Arts School Majors
'''
design_music = Major(major = 'Composición y Producción Musical', faculty=design)
design_music.save()

design_product = Major(major = 'Diseño de Producto e Innovación', faculty=design)
design_product.save()
'''
-----------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
Business and managment school Majors
'''
AdminEmpre = Major(major='Administración de Empresas con Especialización en Transformación Digital', faculty=business)
AdminEmpre.save()

FoodMark = Major(major='Food Business and Marketing', faculty=business)
FoodMark.save()

InterMark = Major(major='International Marketing and Business Analytics', faculty=business)
InterMark.save()
'''
-----------------------------------------------------------------------------------------------------------------------------------------------
'''

dummy_admin = User()
dummy_admin.email = 'gar181469@uvg.edu.gt'
dummy_admin.set_password('doug123')
dummy_admin.first_name = 'Douglas'
dummy_admin.last_name = 'Barrios'
dummy_admin.age = 30
dummy_admin.phone_number = '123456'
dummy_admin.major = computer_science
dummy_admin.is_staff = True
dummy_admin.save()

dummy_user = User()
dummy_user.college_id = '18762'
dummy_user.email = 'val18762@uvg.edu.gt'
dummy_user.set_password('dummyuser123')
dummy_user.first_name = 'Ricardo Antonio'
dummy_user.last_name = 'Valenzuela Avila'
dummy_user.age = 20
dummy_user.phone_number = '56952549'
dummy_user.major = computer_science
dummy_user.is_staff = False
dummy_user.cv.save('Ricardo Antonio_Valenzuela Avila_CV.pdf', File(open('./assets/cv/cv.pdf', 'rb')))
dummy_user.profile_picture.save('Tono.jpg', File(open('./assets/Tono.jpg', 'rb')))
dummy_user.save()   

'''
'''

'''
=============================================================================================
'''

req1 = ProjectRequest()
req1.company_name = 'Mcdonald''s'
req1.project_name = 'Mc en la UVG'
req1.description = '''Debido al nuevo edificio (CIT), 
como empresa nos gustaria hacercarnos a la universidad y 
generar una relacion para que los estudiantes tengan la opcion de 
degustar nuestros producos al alcance de la mano'''
req1.requirements = 'Ser estudiante de 4to ano de Ingenieria en alimentos o carrera afin'
req1.phone_number = '1770'
req1.email_address = 'val18762@uvg.edu.gt'
req1.company_address = 'Ciudad de Guatemala'
req1.about_us = 'Ya deberias saberlo we'
req1.major = computer_science
req1.tags = 'Colesterol  Diabetes  Cocacola  Rinones  Obesidad  UVG  Cardiaco  F'
req1.save()

link = ProjectRequestLinks()
link.link = 'https://mcdonalds.com.gt/'
link.project_request = req1
link.save()

img1 = ProjectRequestImages()
img1.ifk = req1
img1.image.save('mc1.jpeg', File(open('./assets/mc1.jpeg', 'rb')))
img1.save()

img2 = ProjectRequestImages()
img2.ifk = req1
img2.image.save('mc2.jpg', File(open('./assets/mc2.jpg', 'rb')))
img2.save()

img3 = ProjectRequestImages()
img3.ifk = req1
img3.image.save('mc1.jpeg', File(open('./assets/mc3.jpg', 'rb')))
img3.save()

img4 = ProjectRequestImages()
img4.ifk = req1
img4.image.save('mc4.jpeg', File(open('./assets/mc4.jpeg', 'rb')))
img4.save()

'''
=====================================================================================================================
'''

req2 = ProjectRequest()
req2.company_name = 'Excel Automotriz'
req2.project_name = 'Carros electricos en Guatemala'
req2.description = '''Dado que la gasolina es uno de los factores que mas afecta a los guatemaltecos, 
nos gustaria introducir el uso de automoviles electricos en Guatemala.'''
req2.requirements = 'Ser estudiante de 5to ano de Ingenieria en Mecanica o carrera afin'
req2.phone_number = '22778200'
req2.email_address = 'val18762@uvg.edu.gt'
req2.company_address = 'Km 14.5 Calzada Roosevelt 5-86, Zona 3 de Mixco'
req2.about_us = 'Somos la empresa líder de la industria automotriz de la región'
req2.major = computer_science
req2.tags = 'Carros  Mecanico  Mecanica  Manos sucias  GG'
req2.save()

link = ProjectRequestLinks()
link.link = 'https://excelautomotriz.com/guatemala/'
link.project_request = req2
link.save()

img1 = ProjectRequestImages()
img1.ifk = req2
img1.image.save('ex1.jpeg', File(open('./assets/ex1.jpg', 'rb')))
img1.save()

img2 = ProjectRequestImages()
img2.ifk = req2
img2.image.save('ex2.jpg', File(open('./assets/ex2.jpeg', 'rb')))
img2.save()

img3 = ProjectRequestImages()
img3.ifk = req2
img3.image.save('ex3.jpeg', File(open('./assets/ex3.jpeg', 'rb')))
img3.save()

'''
=======================================================================================================================
'''