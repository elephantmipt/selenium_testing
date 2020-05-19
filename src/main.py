import argparse
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.utils import set_city_to_moscow
from src.sign_in_test import (
    test_sign_in_code, test_sign_in_form_phone_number,
)


def test_hipsta_bread(browser):
    """check if there is hipsta buckwheat bread near you"""

    browser.get("https://eda.yandex/")
    set_city_to_moscow(browser)
    text_field = \
        browser.find_element_by_xpath(
            """//*[@id="root"]/div/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/input"""
        )
    text_field.send_keys("гречка")
    time.sleep(2)
    hint = browser.find_element_by_xpath(
        "//*[@id=\"react-autowhatever-1--item-0\"]/div"
    )
    assert hint is not None
    assert "гречка" in hint.text.lower()
    hint.click()
    time.sleep(2)
    hipsta_bread_card = \
        browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div"
        )
    assert "бездрожжевой" in hipsta_bread_card.text.lower()


def test_coffee(browser: webdriver.Chrome):
    browser.get("https://eda.yandex/")
    set_city_to_moscow(browser)
    text_field = \
        browser.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div/div[1]/div/div/"
            "div[4]/div[2]/div/div[1]/div[2]/input"
        )
    text_field.send_keys("черный")
    time.sleep(2)
    browser.find_element_by_xpath(
        "//*[@id=\"react-autowhatever-1--item-0\"]/div"
    ).click()
    time.sleep(2)
    latte_card = browser.find_element_by_xpath(
        "//*[@id=\"root\"]/div/div/div[1]/div/div/div[1]/div[2]/"
        "div/div[2]/div/div[1]/div/div[2]/div[3]/div/div"
    )
    assert "матча" in latte_card.text.lower()


def test_city_change(browser: webdriver.Chrome):
    browser.get("https://eda.yandex/")
    browser.find_element_by_xpath(
        "//*[@id=\"root\"]/div/header/div/div[3]"
    ).click()
    time.sleep(0.5)
    browser.find_element_by_xpath(
        "/html/body/div[3]/div/div[2]/div/div[2]"
    ).click()
    city = browser.find_element_by_xpath(
        "//*[@id=\"root\"]/div/header/div/div[3]"
    )
    assert city.text == "Санкт-Петербург"


def main(args):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    test_hipsta_bread(browser)
    test_sign_in_form_phone_number(browser)
    test_sign_in_code(browser)
    test_coffee(browser)
    test_city_change(browser)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)
