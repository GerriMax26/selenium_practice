from selenium import webdriver

from selenium.webdriver.common.by import By
import time
import math

link = 'https://SunInJuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    
    y = calc(x)
    
    
    input_answer = browser.find_element(By.ID,'answer')
    input_answer.send_keys(y)
    
    checkbox = browser.find_element(By.ID,'robotCheckbox')
    checkbox.click()
    
    
    button = browser.find_element(By.CLASS_NAME,'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)
    
    radiobutton = browser.find_element(By.ID,'robotsRule')
    radiobutton.click()
    

    button.click()
    
    
finally:
    time.sleep(10)
    browser.quit()    