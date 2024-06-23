from hw_11.data.user import User
from hw_11.pages.registration_page import RegistrationFormPage


def test_student_registration_form():
    registration_page = RegistrationFormPage()
    masha = User(first_name='Masha', last_name='Www', email='test@gmail.com', gender='Female',
                 phone='1234456789', date_of_birth_day='11', date_of_birth_month='May', date_of_birth_year='1999',
                 subject='Maths', hobby='Sports', picture='picture.jpg',
                 address='Quitzon Common, South Kraigville', state='NCR', city='Delhi')
    registration_page.open()
    registration_page.register(masha)
    registration_page.should_have_registered(masha)
