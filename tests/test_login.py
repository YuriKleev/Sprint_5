from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators
from url import *

def fill_reg_fields (self,email,password):     # функция для заполнения полей ввода на странице входа
    self.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    self.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    return self

class TestLoginStellarBurgers:

    def test_login_via_main_page(self,driver,registration_user):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    def test_login_via_profile_button(self,driver,registration_user):
        driver.get(main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    def test_login_via_reg_form(self,driver,registration_user):
        driver.get(registration_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_REG_PAGE))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_REG_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    def test_login_via_restore_password_page(self,driver,registration_user):
        driver.get(restore_password_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_RESTORE_PAGE))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_RESTORE_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
