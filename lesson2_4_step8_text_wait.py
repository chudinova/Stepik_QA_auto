import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))

    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    input_value = int(browser.find_element(By.ID, 'input_value').text)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(calc(input_value))

    submit_button = browser.find_element(By.XPATH, '//button [text() = "Submit"]')
    submit_button.click()

finally:

    time.sleep(10)
    browser.quit()
