import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/alert_accept.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value').text
    value = calc(x)

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(value)

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(15)
