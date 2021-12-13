import time
import pytest
from pom.training_ground.main_page import MainPage


@pytest.mark.usefixtures('setup')
@pytest.mark.skip
class TestLec1:

    def test_main_page(self):

        main_page = MainPage(self.driver)
        input1 = main_page.get_input1()
        input1.send_keys("Hello World")

        btn1 = main_page.get_btn1()
        btn1.click()
        time.sleep(5)



