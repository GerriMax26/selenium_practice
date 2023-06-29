from selenium import webdriver

from selenium.webdriver.common.by import By

import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = ' http://suninjuly.github.io/get_attribute.html'

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID,'treasure')

    x = x_element.get_attribute('valuex')

    y = calc(x)

    result = browser.find_element(By.ID,'answer')
    result.send_keys(y)

    checkbox = browser.find_element(By.ID,'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID,'robotsRule')
    radiobutton.click()

    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
        