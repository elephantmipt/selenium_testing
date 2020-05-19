from selenium import webdriver
import time


def set_city_to_moscow(browser: webdriver.Chrome):
    """change your city to Moscow"""
    browser.get("https://eda.yandex/")
    browser.find_element_by_xpath(
        "//*[@id=\"root\"]/div/header/div/div[3]"
    ).click()
    time.sleep(0.5)
    browser.find_element_by_xpath(
        "/html/body/div[3]/div/div[2]/div/div[1]"
    ).click()
    time.sleep(3)  # waiting page
    # load in case you are not in Moscow
