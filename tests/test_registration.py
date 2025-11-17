from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators
from helper import *
from url import profile_page

class TestRegistrationStellarBurgers:

    def test_registration_new_user_valid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_BUTTON_ON_LOGIN_PAGE))
        driver.find_element(*Locators.REG_BUTTON_ON_LOGIN_PAGE).click()
        name, email, password = generate_registration_data(8)
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON_ON_REG_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    def test_registration_new_user_invalid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_BUTTON_ON_LOGIN_PAGE))
        driver.find_element(*Locators.REG_BUTTON_ON_LOGIN_PAGE).click()
        name, email, password = generate_registration_data(4)
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON_ON_REG_PAGE).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ERROR_INCORRECT_PASSWORD))
        #assert driver.find_element(*Locators.ERROR_BORDER).get_attribute('border')=='#e52b1a'
