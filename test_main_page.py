from random import randint

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_auth_fail_with_random_credentials(browser):
    link = "https://beeline.ru"

    browser.get(link)
    browser.implicitly_wait(10)

    enter_button = browser.find_element(By.CSS_SELECTOR, '[button.MgQFWr Ynb9Xm mS4uL4]')
    enter_button.click()

    enter_with_password_button = browser.find_element(By.XPATH, '//span[text()="С постоянным паролем"]')
    enter_with_password_button.click()

    login_enter_field = browser.find_element(By.NAME, 'login')
    login_enter_field.send_keys(randint(9270000000, 9279999999))

    password_enter_field = browser.find_element(By.NAME, 'password')
    password_enter_field.send_keys(randint(100000, 199999))

    auth_submit_button = browser.find_element(By.CLASS_NAME, 'd3jkWo')
    auth_submit_button.click()

    wrong_login_or_password_message = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div[2]/div/div[1]/div[2]')

    assert wrong_login_or_password_message.is_displayed()
