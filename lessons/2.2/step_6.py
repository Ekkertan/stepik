import math
import time

from selenium import webdriver

url = 'http://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(url)

    x = browser.find_element_by_id('input_value').text
    value = calc(x)

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(value)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button.click()

    time.sleep(10)
