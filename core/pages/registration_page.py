import os
import time
from pathlib import Path

from selene import browser, have, command, be


class RegistrationPage:

    def open(self, url):
        browser.open(url)
        return self  # Возвращает объект для цепочной работы

    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name).press_tab()
        return self  # Возвращаем объект для цепочной работы

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name).press_tab()
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def select_gender(self, gender):
        if gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()
        return self

    def fill_user_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        time.sleep(1)
        browser.element('select.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').click()
        browser.element('select.react-datepicker__month-select').click()
        m=int(month)-1
        browser.element(f'[value="{m}"]').click()
        browser.element(f'.react-datepicker__day--00{day}').click()
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def select_hobby(self, hobby):
        if hobby == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
        elif hobby == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
        else:
            browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
        return self

    def upload_picture(self, picture_path):
        img=str(Path(__file__).parent.parent.parent.joinpath(f'resources/{picture_path}'))
        browser.element("#uploadPicture").send_keys(img)
        return self

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def select_state_and_city(self, state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, user):
        browser.element('.table-responsive').should(have.text(f"{user.first_name} {user.last_name}"))
        browser.element('.table-responsive').should(have.text(user.email))
        browser.element('.table-responsive').should(have.text(user.gender))
        browser.element('.table-responsive').should(have.text(user.number))
        browser.element('.table-responsive').should(have.text(f"{user.day} {user.month},{user.year}"))
        browser.element('.table-responsive').should(have.text(user.subject))
        browser.element('.table-responsive').should(have.text(user.hobby))
        browser.element('.table-responsive').should(have.text('dog.jpeg'))
        browser.element('.table-responsive').should(have.text(user.address))
        browser.element('.table-responsive').should(have.text(f"{user.state} {user.city}"))

    def register(self, user):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_user_number(user.number)
        self.fill_date_of_birth(user.year, user.month, user.day)
        self.fill_subject(user.subject)
        self.select_hobby(user.hobby)
        self.upload_picture(user.picture)
        self.fill_current_address(user.address)
        self.select_state_and_city(user.state, user.city)
        self.submit()


