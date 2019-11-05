import time

from selenium import webdriver

from lessons.utils import calc

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(url)
    button = browser.find_element_by_tag_name('button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    value = calc(x)

    input_element = browser.find_element_by_id('answer')
    input_element.send_keys(value)

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(15)
