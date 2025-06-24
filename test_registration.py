from registration_page import RegistrationPage

def test_demoqa():
    registration_page = RegistrationPage()

    registration_page.open() \
        .fill_first_name('Natasha') \
        .fill_last_name('Sidorova') \
        .fill_email('natasha147@mail.ru') \
        .select_gender('Female') \
        .fill_user_number('8965201454') \
        .fill_date_of_birth('1977', '3', '3') \
        .fill_subject('English') \
        .select_hobby('Sports') \
        .upload_picture('dog.jpeg') \
        .fill_current_address('Moscow, Line') \
        .select_state_and_city('NCR', 'Delhi') \
        .submit()

    registration_page.should_have_registered('Natasha', 'Sidorova', 'natasha147@mail.ru')