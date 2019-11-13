import math
import time

import pytest

invalid_text_parts = []


@pytest.mark.parametrize('lesson_id', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_feedback(lesson_id, browser):
    url = f'https://stepik.org/lesson/{lesson_id}/step/1'
    browser.get(url)

    answer = math.log(int(time.time()))
    browser.implicitly_wait(5)
    area = browser.find_element_by_tag_name('textarea')
    area.send_keys(str(answer))

    button = browser.find_element_by_class_name('submit-submission')
    button.click()

    browser.implicitly_wait(5)
    hint_element = browser.find_element_by_class_name('smart-hints__hint')

    hint_text = hint_element.text
    if hint_text != 'Correct!':
        invalid_text_parts.append(hint_text)
        raise ValueError(''.join(invalid_text_parts))
