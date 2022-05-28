import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

trollface_button = browser.find_element(By.CLASS_NAME, 'trollface')
trollface_button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

input_value = int(browser.find_element(By.ID, 'input_value').text)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(calc(input_value))

submit_button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
submit_button.click()

time.sleep(10)
browser.quit()
