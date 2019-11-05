import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lessons.utils import calc

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(url)

    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'),
                                                                                               '$100'))
    button = browser.find_element_by_id('book')
    button.click()

    browser.implicitly_wait(5)

    x = browser.find_element_by_id('input_value').text
    value = calc(x)

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(value)

    button = browser.find_element_by_tag_name("button[type='submit']")
    button.click()

    time.sleep(60)
