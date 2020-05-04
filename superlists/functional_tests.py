"""
Functional Test corresponds to the user story.
This file contains unittests for the functional part.

NewVisitorTest tests the behaviour of the website.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do lists', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # He types 'Buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates, and now the page lists
        # 1. 'Buy peacock feathers' as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. Buy peacock feathers'
                            for row in rows))

        # There is still a text box inviting him to add another item.
        # He enters 'Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items in her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. Buy peacock feathers',
                      [row.text for row in rows])
        self.assertIn('2. Use peacock feathers to make a fly',
                      [row.text for row in rows])

        # Marcel wonders whether the site will remember his list.
        # Then hhe sees that the site has generated a unique URL
        # for his list -- there is some
        # explanatory text to that effect.

        self.fail('Finish the test')
        # He visits that URL - his to-do list is still there

        # Satisfied. Quits the browser.


if __name__ == '__main__':
    unittest.main()
