from faculties.models import Faculty
from majors.models import Major
from users.models import User

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
dummy_admin.email = 'dummyadmin@uvg.edu.gt'
dummy_admin.set_password('dummy123')
dummy_admin.first_name = 'Dummy'
dummy_admin.last_name = 'User'
dummy_admin.age = 30
dummy_admin.phone_number = 'Admin'
dummy_admin.major = biomedical
dummy_admin.is_staff = True
dummy_admin.save()

dummy_user = User()
dummy_user.email = 'dummyuser@uvg.edu.gt'
dummy_user.set_password('dummyuser123')
dummy_user.first_name = 'Dummy'
dummy_user.last_name = 'User'
dummy_user.age = 30
dummy_user.phone_number = '1234'
dummy_user.major = biomedical
dummy_user.is_staff = False
dummy_user.save()


'''

'''











