import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List



#@pytest.mark.usefixtures('setup')
class BasePage:

    def __init__(self, driver):
        print(' --- init BasePage ---')
        self.driver: webdriver = driver
        self.wait = WebDriverWait(driver, 10, 0.5)  # WebDriverWait(driver, time_to_wait, duration)

    def do_send_keys(self, locator, text):
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def is_clickable(self, locator) -> WebElement:
        print(' --- is_clickable ---')
        return self.wait.until(ec.element_to_be_clickable(locator))

    # Waiting on element and return WebElement if it is visible
    def is_visible(self, locator) -> WebElement:
        print(' --- is_visible ---')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def are_visible(self, locator) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def is_present(self, locator) -> WebElement:
        print(' --- is_present ---')
        return self.wait.until(ec.presence_of_element_located(locator))

    def are_presented(self, locator) -> List[WebElement]:
        print(' --- are_present ---')
        return self.wait.until(ec.presence_of_all_elements_located(locator))

