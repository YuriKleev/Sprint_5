from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators

class TestConstructorStellarBurgers:

    def test_selector_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SELECTOR_SAUCES))
        driver.find_element(*Locators.SELECTOR_SAUCES).click()
        driver.find_element(*Locators.SELECTOR_BUNS).click()
        assert 'tab_tab_type_current' in driver.find_element(*Locators.SELECTOR_BUNS).get_attribute('class')

    def test_selector_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SELECTOR_SAUCES))
        driver.find_element(*Locators.SELECTOR_SAUCES).click()
        assert 'tab_tab_type_current' in driver.find_element(*Locators.SELECTOR_SAUCES).get_attribute('class')

    def test_selector_fillings(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SELECTOR_FILLINGS))
        driver.find_element(*Locators.SELECTOR_FILLINGS).click()
        assert 'tab_tab_type_current' in driver.find_element(*Locators.SELECTOR_FILLINGS).get_attribute('class')
