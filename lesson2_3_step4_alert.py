import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

alert_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
alert_button.click()

confirm = browser.switch_to.alert
confirm.accept()

input_value = int(browser.find_element(By.ID, 'input_value').text)

answer_value = calc(input_value)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(answer_value)

submit_button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
submit_button.click()

time.sleep(10)
browser.quit()
