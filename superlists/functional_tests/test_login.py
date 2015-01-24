import time
from unittest import skip
from selenium.webdriver.support.ui import WebDriverWait
from .base import FunctionalTest

TEST_EMAIL = "edith@mockmyid.com"

class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail("could not find window")

    @skip
    def test_login_with_persona(self):
        # Edith goes to the awesome superlists site
        # And notices a "sign in" link for the first time.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id("id_login").click()

        # A persona login appears
        self.switch_to_new_window("Mozilla Persona")

        # Edith logs in which her email address
        ## Use mockmyid.com for test email
        self.browser.find_element_by_id(
            "authentication_email"
        ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name("button").click()

        # The persona window closes
        self.switch_to_new_window("To-Do")

        # She can see that she is logged in
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Refreshing the page, she sees it's a real session login,
        # not just a one-off for that page
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)

        # The 'logged out' status also persists after a refresh
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)
