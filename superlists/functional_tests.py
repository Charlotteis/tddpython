import unittest
from selenium import webdriver


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app,
        # she goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mentions to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item straight away

        # She types "buy peacock feathers" into a text box

        # When she hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "use peackock feathers to make a fly"

        # The page updates again, and now she shows both items on her list

        # Edith wonders whether the site will remember her list.
        # She sees that the site

        # Has generated a unique URL for her
        # -- there is some explantory text to that
        # effect.

        # She visits that URL - her todo list is still there

        # Satisfied, she goes back to sleep
        self.browser.quit()

if __name__ == "__main__":
    unittest.main(warnings="ignore")
