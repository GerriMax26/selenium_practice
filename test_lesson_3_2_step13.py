import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestForm(unittest.TestCase):
    def test_1(self):
    
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element(By.CSS_SELECTOR, 'input.first:required')
        input_first_name.send_keys('Ivan')

        input_last_name = browser.find_element(By.CSS_SELECTOR, 'input.second:required')
        input_last_name.send_keys('Petrov')

        input_email = browser.find_element(By.CSS_SELECTOR, 'input.third:required')
        input_email.send_keys('123@mail.ru')


        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)



if __name__ == '__main__':
    unittest.main()