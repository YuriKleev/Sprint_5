from faker import Faker
from random import randint
from locators import Locators

faker = Faker()

def generate_registration_data(password_length):     # генератор тестовых данных (имя, Email, пароль)
    name=faker.first_name()
    email='yuri_kleev_35_'+str(randint(100,999))+'@ya.ru'
    password=faker.password(length=password_length, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password

def fill_reg_fields (self,email,password):     # функция для заполнения полей Email и пароль на странице входа
    self.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    self.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    return self
