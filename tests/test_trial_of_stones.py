import time
import pytest
from pom.training_ground.main_page import MainPage
from pom.training_ground.trial_of_the_stones import TrialOfTheStones


@pytest.mark.usefixtures('setup')
class TestTrialOfStones:

    def test_trial_of_stones(self):

        trial = TrialOfTheStones(self.driver)
        input1 = trial.get_input1()
        input1.send_keys("rock")

        btn1 = trial.get_btn1()
        btn1.click()

        pass_field = trial.get_password_input1()

        input2 = trial.get_input2()
        btn2 = trial.get_btn2()
        input2.send_keys(pass_field.text)
        btn2.click()

        success_field1 = trial.get_success_banner1()

        assert success_field1.text == 'Success!'

        total_fields = [item.text for item in trial.get_total_wealth_fields()]
        name_fields = [item.text for item in trial.get_names_of_wealth_fields()]

        merchant_dictionary = dict(zip(name_fields, total_fields))

        max_balance = 0
        winner_name = ''
        for name, balance in merchant_dictionary.items():
            balance = int(balance)
            if balance > max_balance:
                max_balance = balance
                winner_name = name

        input3 = trial.get_input3()
        btn3 = trial.get_btn3()
        input3.send_keys(winner_name)
        btn3.click()

        success_field2 = trial.get_success_banner2()

        assert success_field2.text == 'Success!'

        btn_check = trial.get_btn_check()
        btn_check.click()

        banner_complete = trial.get_banner_complete()

        assert banner_complete.text == 'Trial Complete'

        time.sleep(3)
