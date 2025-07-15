import os
import time
from pathlib import Path

import allure
from selene import browser, have, command, be


class RegistrationPage:

    @allure.step('Открываем сайт')
    def open(self, url):
        browser.open(url)
        return self  # Возвращает объект для цепочной работы

    @allure.step('Вводим имя')
    def fill_first_name(self, first_name):
        browser.element('#firstName').type(first_name).press_tab()
        return self  # Возвращаем объект для цепочной работы

    @allure.step('Вводим фамилию')
    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name).press_tab()
        return self

    @allure.step('Вводим почту')
    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    @allure.step('Пол')
    def select_gender(self, gender):
        if gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()
        return self

    @allure.step('Номер телефона')
    def fill_user_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    @allure.step('Дата рождения')
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        time.sleep(1)
        with allure.step('Заполняем год'):
            browser.element('select.react-datepicker__year-select').click()
            browser.element(f'[value="{year}"]').click()
        with allure.step('Заполняем месяц'):
            browser.element('select.react-datepicker__month-select').click()
            months = [
                "January", "February", "March", "April",
                "May", "June", "July", "August",
                "September", "October", "November", "December"
            ]
            month_number = months.index(month)
            browser.element(f'[value="{month_number}"]').click()
        with allure.step('Заполняем день'):
            browser.element(f'.react-datepicker__day--0{day}').click()
            return self

    @allure.step('Предмет')
    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    @allure.step('Хобби')
    def select_hobby(self, hobby):
        if hobby == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
        elif hobby == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
        else:
            browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
        return self

    @allure.step('Добавляем картинку')
    def upload_picture(self, picture_path):
        img=str(Path(__file__).parent.parent.parent.joinpath(f'resources/{picture_path}'))
        browser.element("#uploadPicture").send_keys(img)
        return self

    @allure.step('Адресс')
    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    @allure.step('Город')
    def select_state_and_city(self, state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    @allure.step('Выбор')
    def submit(self):
        browser.element('#submit').click()
        return self

    @allure.step('Выполняем проверку')
    def should_have_registered(self, user):
        browser.element('.table-responsive').should(have.text(f"{user.first_name} {user.last_name}"))
        browser.element('.table-responsive').should(have.text(user.email))
        browser.element('.table-responsive').should(have.text(user.gender))
        browser.element('.table-responsive').should(have.text(user.number))
        browser.element('.table-responsive').should(have.text(f"{user.birth_day} {user.birth_month},{user.birth_year}"))
        browser.element('.table-responsive').should(have.text(user.subject))
        browser.element('.table-responsive').should(have.text(user.hobby))
        browser.element('.table-responsive').should(have.text('dog.jpeg'))
        browser.element('.table-responsive').should(have.text(user.address))
        browser.element('.table-responsive').should(have.text(f"{user.state} {user.city}"))

    @allure.step('Заполняем форму пользователя')
    def register(self, user):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_user_number(user.number)
        self.fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)
        self.fill_subject(user.subject)
        self.select_hobby(user.hobby)
        self.upload_picture(user.picture)
        self.fill_current_address(user.address)
        self.select_state_and_city(user.state, user.city)
        self.submit()


