import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input_field = browser.find_element(By.ID, 'answer')
input_field.send_keys(y)

robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_checkbox.click()

robot_radio = browser.find_element(By.ID, 'robotsRule')
robot_radio.click()

submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
submit_button.click()
time.sleep(10)

browser.quit()
