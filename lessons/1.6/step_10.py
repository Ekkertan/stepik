import time

from faker import Faker
from selenium import webdriver

fake = Faker()
url = 'http://suninjuly.github.io/registration1.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    inputs = browser.find_elements_by_css_selector('input[required]')
    for input in inputs:
        value = fake.word()
        input.send_keys(value)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    time.sleep(1)

    assert browser.find_element_by_tag_name('h1').text == "Congratulations! You have successfully registered!"
