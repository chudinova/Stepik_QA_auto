from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
first_name_field = browser.find_element(By.CLASS_NAME, "first")
first_name_field.click()
first_name_field.send_keys("Name")

second_name_field = browser.find_element(By.CLASS_NAME, "second")
second_name_field.click()
second_name_field.send_keys("Surname")

email_field = browser.find_element(By.CLASS_NAME, "third")
email_field.click()
email_field.send_keys("email@domain.com")

phone_field = browser.find_element(By.XPATH, 'input[placeholder = "Input your phone:"]')
phone_field.click()
phone_field.send_keys(+79000000000)

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
