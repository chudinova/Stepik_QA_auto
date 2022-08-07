import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_set_answer(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1/"
    browser.get(link)
    browser.implicitly_wait(10)

    enter_field = browser.find_element(By.TAG_NAME, 'textarea')
    # enter_field.click()
    enter_field.send_keys(math.log(int(time.time())))

    submit_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    submit_button.click()

    message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    expected = "Correct!"
    actual = message.text
    assert (expected == actual)
