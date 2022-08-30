from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from pom.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, driver):
        print(' --- init HomePage ---')
        super().__init__(driver)
        driver.get('https://rt-ed.co.il/')

    def __get_selenium_by(self, find: str) -> dict:
        find = find.lower()
        locating = {'odot': (By.LINK_TEXT, 'אודות'),
                    'zorkesher': (By.LINK_TEXT, 'צור קשר'),
                    'all_f_stack': (By.XPATH, '//*[@id="primar-menu"]/li'),
                    'cyber': (By.LINK_TEXT, 'Cyber'),
                    'cybers': (By.XPATH, '//*[@id="primar-menu"]/li[8]/ul/li'),
                    'menu': (By.XPATH, '//*[@id="primar-menu"]/li')}
        return locating[find]

    def go_to_zorkesher(self):
        print('go_to_zorkesher')
        self.do_click(self.zorkesher)

    def go_to_odot(self):
        print('go_to_odot')
        # self.do_click(self.odot)
        self.is_clickable(self.odot).click()

    """
    def give_me_odot_btn(self):
        return self.is_clickable(self.odot)
    """

    def give_me_webelement(self, name: str):
        return self.is_clickable(self.__get_selenium_by(name))

    def give_me_list_of_webelement(self, name: str) -> List[WebElement]:
        return self.are_visible(self.__get_selenium_by(name))

    def get_elem(self, locator):
        return self.driver.find_element(locator)

    def give_cyber_elements(self) -> List[WebElement]:
        self.do_click(self.__get_selenium_by('cyber'))
        return self.are_visible(self.__get_selenium_by('cybers'))
