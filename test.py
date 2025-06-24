import os
from selene import browser, have


def test_demoqa():
    #открыть браузер
    browser.open('https://demoqa.com/automation-practice-form')

    #заполнить поля
    browser.element('#firstName').type('Natasha').press_tab()
    browser.element('#lastName').type('Sidorova').press_tab()
    browser.element('#userEmail').type('natasha147@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('8965201454')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1977"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="3"]').click()
    browser.element('[aria-label="Choose Sunday, April 3rd, 1977"]').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('dog.jpeg'))
    browser.element('#currentAddress').type('Moscow, Line')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    #отправить данные
    browser.element('#submit').click()

    #проверить данные
    browser.element('.table-responsive').should(have.text('Natasha Sidorova'))
    browser.element('.table-responsive').should(have.text('natasha147@mail.ru'))
    browser.element('.table-responsive').should(have.text('Female'))
    browser.element('.table-responsive').should(have.text('8965201454'))
    browser.element('.table-responsive').should(have.text('03 April,1977'))
    browser.element('.table-responsive').should(have.text('English'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('dog.jpeg'))
    browser.element('.table-responsive').should(have.text('Moscow, Line'))
    browser.element('.table-responsive').should(have.text('NCR Delhi'))