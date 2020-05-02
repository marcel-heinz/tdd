"""
Functional Test corresponds to the user story.
"""

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Marcel has heard a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # He is invited to enter a to-do item straight away

        # She types 'Buy peacock feathers' into a text box

        # When she hits enter, the page updates, and now the page lists
        # 1. 'Buy peacock feathers' as an item in the to-do list

        # There is still a text box inviting her to add another item.
        # She enters 'Use peacock feathers to make a fly'

        # The page updates again, and now shows both items in her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there

        # Satisfied. Quits the browser.


if __name__ == '__main__':
    unittest.main()
