import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

firstname_field = browser.find_element(By.NAME, 'firstname')
firstname_field.send_keys('Name')

lastname_field = browser.find_element(By.NAME, 'lastname')
lastname_field.send_keys('Lastname')

email_field = browser.find_element(By.NAME, 'email')
email_field.send_keys('email@domain.com')

file_add_button = browser.find_element(By.NAME, 'file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file_add_button.send_keys(file_path)

submit_button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
submit_button.click()

time.sleep(10)
browser.quit()
