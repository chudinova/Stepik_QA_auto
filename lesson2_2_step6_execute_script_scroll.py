import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

x_value = int(browser.find_element(By.ID, 'input_value').text)
answer = calc(x_value)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(answer)

robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
robot_checkbox.click()

robot_rule_radio = browser.find_element(By.ID, 'robotsRule')
robot_rule_radio.click()

submit_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
submit_button.click()

time.sleep(10)
browser.quit()
