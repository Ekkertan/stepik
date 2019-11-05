import os
import time
from faker import Faker

from selenium import webdriver

url = 'http://suninjuly.github.io/file_input.html'
fake = Faker()

with webdriver.Chrome() as browser:
    browser.get(url)

    for element in browser.find_elements_by_css_selector('input[type="text"][required]'):
        value = fake.word()
        print(f'{element}\n{value}')
        element.send_keys(value)

    load_button = browser.find_element_by_css_selector('input[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    load_button.send_keys(file_path)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    time.sleep(15)
