import time
import unittest

from selenium import webdriver


class RegistrationFormTest(unittest.TestCase):
    def check_registration(self, url):
        with webdriver.Chrome() as browser:
            browser.get(url)

            input_classnames = ('first', 'second', 'third')
            input_values = ('Ivan', 'Bobrov', 'i.bobrov@fakemail.com')

            for input_classname, input_value in zip(input_classnames, input_values):
                # zip возвращает по одному элементу из каждого кортежа
                # (любого итерируемого объекта, на самом деле), переданного в аргументах.
                # Подробнее можно посмотреть в докумнентации https://docs.python.org/3.3/library/functions.html#zip
                #
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

            self.assertEqual(browser.find_element_by_tag_name('h1').text,
                             "Congratulations! You have successfully registered!")

    def test_registration1_positive(self):
        url = 'http://suninjuly.github.io/registration1.html'
        self.check_registration(url)

    def test_registration2_negative(self):
        url = 'http://suninjuly.github.io/registration2.html'
        self.check_registration(url)


if __name__ == '__main__':
    unittest.main()
