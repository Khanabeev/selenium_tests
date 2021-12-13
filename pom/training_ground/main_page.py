from selenium.webdriver.remote.webelement import WebElement
from base.selenium_base import SeleniumBase
from typing import List

from base.utils import Utils


class MainPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.input1_locator_id = 'ipt1'
        self.input2_locator_id = 'ipt2'
        self.btn1_locator_id = 'b1'
        self.product1_locator_xpath = "//b[text()='Product 1']"

    def get_input1(self) -> WebElement:
        return self.is_visible('id', self.input1_locator_id, "Input 1")

    def get_btn1(self) -> WebElement:
        return self.is_visible('id', self.btn1_locator_id, "Button 1")


