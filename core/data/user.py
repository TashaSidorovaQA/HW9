from dataclasses import dataclass
@dataclass
class User:
    first_name: str = 'Natasha'
    last_name: str = 'Sidorova'
    email: str = 'natasha147@mail.ru'
    gender: str = 'Female'  # Значение по умолчанию
    number: str = '8965201454'
    birth_year: str = '1977'
    birth_month: str = 'March'
    birth_day: str = '03'
    subject: str = 'English'
    hobby: str = 'Sports'
    picture: str = 'dog.jpeg'
    address: str = 'Moscow, Line'
    state: str = 'NCR'
    city: str = 'Delhi'
