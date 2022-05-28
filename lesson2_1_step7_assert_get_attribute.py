import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

treasure_icon = browser.find_element(By.ID, 'treasure')
valuex_value = treasure_icon.get_attribute('valuex')
function_answer = calc(valuex_value)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(function_answer)

robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_checkbox.click()

robot_rule_radio = browser.find_element(By.ID, 'robotsRule')
robot_rule_radio.click()

submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
submit_button.click()

time.sleep(10)
browser.quit()
