import time

from faker import Faker     # Пакет для генерации фэйковых данных, https://faker.readthedocs.io/en/latest/index.html
from selenium import webdriver


with webdriver.Chrome() as browser:
    fake = Faker()
    url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)

    input_classnames = ('first', 'second', 'third')
    for input_classname in input_classnames:
        # на каждой итерации цикла последовательно создаются селекторы
        # .first[required], .second[required] и .third[required]
        # Про f-strings в python можно почитать тут: https://realpython.com/python-f-strings/
        # (на русском - например, тут: https://python-scripts.com/f-strings )
        selector = f'.{input_classname}[required]'

        element = browser.find_element_by_css_selector(selector)
        print(element)
        value = fake.word()
        element.send_keys(value)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    time.sleep(1)

    assert browser.find_element_by_tag_name('h1').text == "Congratulations! You have successfully registered!"
