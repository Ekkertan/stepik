import time

from selenium import webdriver


with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)

    input_classnames = ('first', 'second', 'third')
    input_values = ('Ivan', 'Bobrov', 'i.bobrov@fakemail.com')
    for input_classname, input_value in zip(input_classnames, input_values):
        # на каждой итерации цикла последовательно создаются селекторы
        # .first[required], .second[required] и .third[required]
        # Про f-strings в python можно почитать тут: https://realpython.com/python-f-strings/
        # (на русском - например, тут: https://python-scripts.com/f-strings )
        selector = f'.{input_classname}[required]'

        element = browser.find_element_by_css_selector(selector)
        element.send_keys(input_value)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

    time.sleep(1)

    assert browser.find_element_by_tag_name('h1').text == "Congratulations! You have successfully registered!"
