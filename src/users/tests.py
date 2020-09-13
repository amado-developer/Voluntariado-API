from django.test import TestCase
from users.models import User
from majors.models import Major
from faculties.models import Faculty

class UserTypeTest(TestCase):
    def setUp(self):
        faculty = Faculty.objects.create(faculty='testFaculty')
        major = Major.objects.create(major='testMajor', faculty=faculty)
        User.objects.create(email='testadminuser@test.com', 
                                first_name='testAdminFirstName', 
                                last_name='testAdminLastName', 
                                profile_picture=None,
                                phone_number='12345678',
                                password= 'testadminpwd', 
                                age=18,
                                major = major,
                                is_staff=True
                                )

        User.objects.create(email='teststudentuser@test.com', 
                                first_name='testStudentFirstName', 
                                last_name='testStudentLastName', 
                                profile_picture=None,
                                phone_number='187654321',
                                password= 'teststudentpwd', 
                                age=18,
                                major = major,
                                is_staff=False
                                )

    def test_is_admin_user(self):
        """User is admin or not"""
        admin = User.objects.get(email='testadminuser@test.com')
        self.assertEqual(admin.is_staff, True)
      

    def test_is_student_user(self):
        """User is student or not"""
        student = User.objects.get(email='teststudentuser@test.com')
        self.assertEqual(student.is_staff, False)

