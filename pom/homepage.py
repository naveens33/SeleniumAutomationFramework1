from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from decorators.elements import elements
from pom.basepage import BasePage
from pom.homeselector import Home_Selectors


@elements(Home_Selectors)
class HomePage(BasePage, Exception):

    def __init__(self, driver):
        self.driver = driver
        pass

    def click_sign_in_button(self):
        ele = self.signin_button.find_element()
        pass
        # self._click(self._sign_in_button)

    def do_search(self, search_term):
        self._enter_text(self._search_field, search_term)
        self._enter_text(self._search_field, Keys.ENTER)
