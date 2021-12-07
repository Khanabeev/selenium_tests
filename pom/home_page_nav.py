from selenium.webdriver.remote.webelement import WebElement
from base.selenium_base import SeleniumBase
from typing import List

from base.utils import Utils


class HomePageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '.navbar-nav.mr-auto>li>.nav-link'
        self.NAV_LINK_TEXT = 'Payments,Invoicing,Pricing'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name: str) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
