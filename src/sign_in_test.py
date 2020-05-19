import time
from selenium import webdriver


def test_sign_in_code(browser: webdriver.Chrome):
    browser.get("https://eda.yandex/")
    time.sleep(2)
    browser.find_element_by_xpath(
        "//*[@id=\"root\"]/div/header/div/button"
    ).click()  # click sign in button
    time.sleep(2)
    code_field = browser.find_element_by_xpath(
        "/html/body/div[3]/div/div/div[3]"
        "/div/div[2]/div[4]/input"
    )
    code_field.send_keys("1223")
    assert code_field.get_attribute("value") == "1223"
    code_field.clear()
    code_field.send_keys("122345")
    assert code_field.get_attribute("value") == "1223"


def test_sign_in_form_phone_number(browser: webdriver.Chrome):
    browser.get("https://eda.yandex/")
    time.sleep(2)
    browser.find_element_by_xpath(
        "//*[@id=\"root\"]/div/header/div/button"
    ).click()  # click sign in button
    time.sleep(2)
    phone_field = browser.find_element_by_xpath(
        "/html/body/div[3]/div/div/div[3]"
        "/div/div[2]/div[2]/div/input"
    )
    phone_field.send_keys("0123456789")  # invalid first digits
    assert phone_field.get_attribute("value") == "+7 (789"
    phone_field.clear()
    time.sleep(0.3)
    phone_field.send_keys("01234567890123")  # too long and invalid
    assert phone_field.get_attribute("value") == "+7 (789) 012-3"
    phone_field.clear()
    time.sleep(0.3)
    phone_field.send_keys("7890123554")  # valid
    assert phone_field.get_attribute("value") == "+7 (789) 012-35-54"
    phone_field.clear()
    time.sleep(0.6)
    phone_field.send_keys("78901")  # valid too long
    time.sleep(0.3)
    phone_field.send_keys("23554")  # valid too long
    time.sleep(0.3)
    phone_field.send_keys("9889")
    assert phone_field.get_attribute("value") == "+7 (789) 012-35-54"
