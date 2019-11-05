import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects2.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    num_1 = browser.find_element_by_id('num1').text
    num_2 = browser.find_element_by_id('num2').text
    value = int(num_1) + int(num_2)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(value))

    button = browser.find_element_by_tag_name('button[type="submit"]')
    button.click()

    time.sleep(10)
