from selenium import webdriver
from .base import FunctionalTest


def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass


class SharingTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith goes to the homepage and starts a list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys("Get help\n")

        # She notices a "share this list" option
        share_box = self.browser.find_element_by_css_selector("input[name=email]")
        self.assertEqual(
            share_box.get_attribute("placeholder"),
            "your-friend@example.com"
        )
