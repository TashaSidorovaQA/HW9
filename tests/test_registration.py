import allure
from allure_commons.types import Severity

from core.data.user import User
from core.pages.registration_page import RegistrationPage

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'mininAV')
@allure.feature('Задачи в репозитории')
@allure.story('Просмотр задач авторизованным пользователем')
def test_demoqa():
    with allure.step('Создаем user Natasha'):
        natasha = User()
    registration_page = RegistrationPage()
    registration_page.open("https://demoqa.com/automation-practice-form")
    registration_page.register(natasha)
    registration_page.should_have_registered(natasha)





