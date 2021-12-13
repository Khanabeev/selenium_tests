from selenium.webdriver.remote.webelement import WebElement
from base.selenium_base import SeleniumBase
from typing import List


from base.utils import Utils


class TrialOfTheStones(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.input1_locator_id = 'r1Input'
        self.btn1_locator_id = 'r1Btn'
        self.input2_locator_id = 'r2Input'
        self.btn2_locator_id = 'r2Butn'
        self.input3_locator_id = 'r3Input'
        self.btn3_locator_id = 'r3Butn'
        self.btn_check_locator_id = 'checkButn'
        self.banner_complete_locator_id = 'trialCompleteBanner'

        self.password_input1_locator_xpath = "//div[@id='passwordBanner']/h4"
        self.success_banner1_locator_xpath = "//div[@id='successBanner1']/h4"
        self.success_banner2_locator_xpath = "//div[@id='successBanner2']/h4"
        self.total_wealth_locator_xpath = "//div/label[text()='Total Wealth ($):']/../p"
        self.name_wealth_locator_xpath = "//div/label[text()='Total Wealth ($):']/../span/b"


    def get_input1(self) -> WebElement:
        return self.is_visible('id', self.input1_locator_id, "Input 1")

    def get_btn1(self) -> WebElement:
        return self.is_visible('id', self.btn1_locator_id, "Button 1")

    def get_input2(self) -> WebElement:
        return self.is_visible('id', self.input2_locator_id, "Input 2")

    def get_btn2(self) -> WebElement:
        return self.is_visible('id', self.btn2_locator_id, "Button 2")

    def get_input3(self) -> WebElement:
        return self.is_visible('id', self.input3_locator_id, "Input 3")

    def get_btn3(self) -> WebElement:
        return self.is_visible('id', self.btn3_locator_id, "Button 3")

    def get_btn_check(self) -> WebElement:
        return self.is_visible('id', self.btn_check_locator_id, "Button Check")

    def get_password_input1(self) -> WebElement:
        return self.is_visible('xpath', self.password_input1_locator_xpath)

    def get_success_banner1(self) -> WebElement:
        return self.is_visible('xpath', self.success_banner1_locator_xpath)

    def get_success_banner2(self) -> WebElement:
        return self.is_visible('xpath', self.success_banner2_locator_xpath)

    def get_total_wealth_fields(self) -> List[WebElement]:
        return self.are_visible('xpath', self.total_wealth_locator_xpath)

    def get_names_of_wealth_fields(self) -> List[WebElement]:
        return self.are_visible('xpath', self.name_wealth_locator_xpath)

    def get_banner_complete(self) -> WebElement:
        return self.is_visible('id', self.banner_complete_locator_id)



