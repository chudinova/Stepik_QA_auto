import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'num1').text

num2 = browser.find_element(By.ID, 'num2').text

answer = int(num1) + int(num2)

answer_list = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
answer_list.select_by_value(str(answer))

submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
submit_button.click()

time.sleep(10)
browser.quit()
