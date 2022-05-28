import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

find_link = browser.find_element(by=By.LINK_TEXT, value=str(math.ceil(math.pow(math.pi, math.e) * 10000)))
find_link.click()

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
