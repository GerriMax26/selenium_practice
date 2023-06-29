from selenium import webdriver

from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input_first_name = browser.find_element(By.NAME,'firstname')
    input_first_name.send_keys('Maksim')
    
    input_last_name = browser.find_element(By.NAME,'lastname')
    input_last_name.send_keys('Garaev')
    
    input_email = browser.find_element(By.NAME,'email')
    input_email.send_keys('garaev.maxim2013@yandex.ru')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir,'file.txt')
    
    element = browser.find_element(By.ID,'file')
    element.send_keys(file_path)
    
    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()