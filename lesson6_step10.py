from selenium import webdriver

from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.ui import Select

try:
    link = 'https://suninjuly.github.io/selects1.html'
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    number1 = browser.find_element(By.ID,'num1')
    num1 = int(number1.text)
    
    number2 = browser.find_element(By.ID,'num2')
    num2 = int(number2.text)
    
    result_summ = num1 + num2
    
    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(f'{result_summ}')
    
    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()