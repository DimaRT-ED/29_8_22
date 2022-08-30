import time
from selenium import webdriver
import pytest
from selenium.webdriver.remote.webelement import WebElement

from pom.pages.home_page import HomePage
from typing import List


@pytest.mark.usefixtures('setup')
class TestHomePage:
    @pytest.mark.skip
    def test_zor_kesher_btn(self):
        print('test_zor_kesher_btn')
        home_page = HomePage(self.driver)
        home_page.go_to_zorkesher()
        time.sleep(2)

    @pytest.mark.skip
    def test_odot(self):
        print('test_odot')
        home_page = HomePage(self.driver)
        # home_page.give_me_odot_btn().click()
        home_page.give_me_webelement('odot').click()
        time.sleep(2)

    @pytest.mark.skip
    def test_cyber_btn(self):
        home_page = HomePage(self.driver)
        home_page.give_me_webelement('Cyber').click()
        home_page.driver.save_screenshot(f".\\src\\name.png")
        time.sleep(2)


    def test_cyber_in(self):
        home_page = HomePage(self.driver)
        list: List[WebElement] = home_page.give_cyber_elements()
        for l in list:
            print(l.text)
            time.sleep(2)

    @pytest.mark.skip
    def test_menu(self):
        home_page = HomePage(self.driver)
        list: List[WebElement] = home_page.give_me_list_of_webelement('MEnu')
        for l in list:
            print(l.text)
            time.sleep(2)