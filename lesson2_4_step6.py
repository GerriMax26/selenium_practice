from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/cats.html'

browser = webdriver.Chrome()
browser.get(link)

#Будет исключение NoSuchElementException

browser.find_element(By.ID,'button')
