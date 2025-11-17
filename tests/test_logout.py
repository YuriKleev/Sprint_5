from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators
from helper import fill_reg_fields
from url import login_page

class TestLogoutStellarBurgers:

    def test_transit_to_profile(self,driver,registration_user):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        email,password=registration_user[1],registration_user[2]
        fill_reg_fields (driver,email,password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
