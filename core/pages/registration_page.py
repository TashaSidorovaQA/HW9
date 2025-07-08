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

    def should_have_registered(self, first_name, last_name, email, gender, number, year, month, day, subject, hobby,
                               address, state, city):
        browser.element('.table-responsive').should(have.text(f"{first_name} {last_name}"))
        browser.element('.table-responsive').should(have.text(email))
        browser.element('.table-responsive').should(have.text(gender))
        browser.element('.table-responsive').should(have.text(number))
        browser.element('.table-responsive').should(have.text(f"{day} {month},{year}"))
        browser.element('.table-responsive').should(have.text(subject))
        browser.element('.table-responsive').should(have.text(hobby))
        browser.element('.table-responsive').should(have.text('dog.jpeg'))
        browser.element('.table-responsive').should(have.text(address))
        browser.element('.table-responsive').should(have.text(f"{state} {city}"))
