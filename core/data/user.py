from dataclasses import dataclass
@dataclass
class User:
    first_name: str = 'Natasha'
    last_name: str
    email: str
    gender: str = 'Female'  # Значение по умолчанию
    phone: str = ''
    birth_year: str = '1977'
    birth_month: str = '3'
    birth_day: str = '3'
    subject: str = 'English'
    hobby: str = 'Sports'
    picture: str = 'dog.jpeg'
    address: str = 'Moscow, Line'
    state: str = 'NCR'
    city: str = 'Delhi'
