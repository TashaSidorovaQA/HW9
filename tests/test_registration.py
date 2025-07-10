from core.data.user import User
from core.pages.registration_page import RegistrationPage

def test_demoqa():
    natasha = User()
    registration_page = RegistrationPage()
    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.register(natasha)
    registration_page.should_have_registered(natasha)





