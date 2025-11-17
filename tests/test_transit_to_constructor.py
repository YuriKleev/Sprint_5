from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators
from helper import fill_reg_fields

class TestTransitionToProfileStellarBurgers:

    def test_transit_to_constructor_via_button(self,driver,registration_user):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()        
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CREATE_BURGER))

    def test_transit_to_constructor_via_logo(self,driver,registration_user):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGO_STELLARBURGERS))
        driver.find_element(*Locators.LOGO_STELLARBURGERS).click()        
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CREATE_BURGER))
