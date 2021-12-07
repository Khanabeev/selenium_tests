import time

import pytest

from pom.home_page_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomePageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT

        for i in range(3):
            homepage_nav.get_nav_links()[i].click()
            time.sleep(1)

        assert expected_links == actual_links, 'Validating Nav Links text'


