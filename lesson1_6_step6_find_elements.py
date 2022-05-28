from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements(By.TAG_NAME, "input")
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
