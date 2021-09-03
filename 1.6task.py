from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    # первая страница регистрации
    browser = webdriver.Chrome()
    browser.get(link1)
    input1 = browser.find_element_by_css_selector(".first_block > .form-group.first_class :nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block > .form-group.second_class :nth-child(2)")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block > .form-group.third_class :nth-child(2)")
    input3.send_keys("Email")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.close()
    time.sleep(2)
    browser.quit()

try:
    # вторая страница регистрации
    browser = webdriver.Chrome()
    browser.get(link2)
    input1 = browser.find_element_by_css_selector(".first_block > .form-group.first_class :nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block > .form-group.second_class :nth-child(2)")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block > .form-group.third_class :nth-child(2)")
    input3.send_keys("Email")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.close()
    time.sleep(2)
    browser.quit()
