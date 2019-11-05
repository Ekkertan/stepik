import time

from faker import Faker
from selenium import webdriver

url = 'http://suninjuly.github.io/huge_form.html'
fake = Faker()

with webdriver.Chrome() as browser:
    browser.get(url)

    tags = browser.find_elements_by_tag_name('input')

    for tag in tags:
        value = fake.word(ext_word_list=None)
        tag.send_keys(value)

    button = browser.find_element_by_tag_name('button')
    button.click()

    time.sleep(15)
