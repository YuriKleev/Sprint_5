import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators
from url import main_page

@pytest.fixture (scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1280,720")
    service = Service ('C:/WebDriver/bin/chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(main_page)
    yield browser
    browser.quit()

@pytest.fixture (scope="function")
def registration_user (driver):
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_MAIN_PAGE))
    driver.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_BUTTON_ON_LOGIN_PAGE))
    driver.find_element(*Locators.REG_BUTTON_ON_LOGIN_PAGE).click()
    name, email, password = generate_registration_data(8)
    driver.find_element(*Locators.INPUT_NAME).send_keys(name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.REG_BUTTON_ON_REG_PAGE).click()
    return driver,email,password
