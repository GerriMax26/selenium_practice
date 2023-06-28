from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from fake_useragent import UserAgent
import time, random, json, ast, re, math, os, unittest
#################
# pip freeze > requirements.txt
# pip install -r requirements.txt
#################


url_1 = f"http://suninjuly.github.io/registration1.html"
url_2 = f"http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url_1)
    # в данном случае жестко хардкодим плэйсхолдер. Это не правильно, но все работает. 
    # можно найти все элементы обязательные и в каждый обязательный передать ключи
    # при этом в первом случае - будет 3 обязательных а во втором два и тест упадет.
    first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Petr")
    last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your last name')]").send_keys("Petrov")
    mail = browser.find_element(By.CLASS_NAME, 'form-control.third').send_keys("sssss@ssss.ss")
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    print("First link Done!")

    browser.get(url_2)

    first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Petr")
    last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your last name')]").send_keys("Petrov")
    mail = browser.find_element(By.CLASS_NAME, 'form-control.third').send_keys("sssss@ssss.ss")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    print("Expect - down test")

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()