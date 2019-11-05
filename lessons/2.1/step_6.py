import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(url)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    value = calc(x)

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(value)

    checkbox_element = browser.find_element_by_id('robotCheckbox')
    checkbox_element.click()

    radio_element = browser.find_element_by_id('robotsRule')
    radio_element.click()

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    time.sleep(10)
