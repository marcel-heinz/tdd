"""
Functional Test corresponds to the user story.
This file contains unittests for the functional part.

NewVisitorTest tests the behaviour of the website.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id(
                    'id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Marcel has heard a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do list
        self.assertIn('To-Do App', self.browser.title)
        header_text = self.browser.find_element_by_id('headline').text
        self.assertEqual('Start your To-Do list', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # He types 'Buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When he hits enter, the page updates, and now the page lists
        # 1. 'Buy peacock feathers' as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1. Buy peacock feathers')

        # There is still a text box inviting him to add another item.
        # He enters 'Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items in her list
        self.wait_for_row_in_list_table('1. Buy peacock feathers')
        self.wait_for_row_in_list_table(
            '2. Use peacock feathers to make a fly')

        # Marcel wonders whether the site will remember his list.
        # Then he sees that the site has generated a unique URL
        # for his list -- there is some
        # explanatory text to that effect.

        # self.fail('Finish the test')
        # He visits that URL - his to-do list is still there

        # Satisfied. Quits the browser.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Marcel starts a new to-do list
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Buy peacock feathers')

        # He notices that his list has a unique URL
        marcel_list_url = self.browser.current_url
        self.assertRegex(marcel_list_url, '/lists/.+')
        self.assertIn('To-Do App', self.browser.title)
        header = self.browser.find_element_by_id('headline').text
        self.assertEqual('Your To-Do List', header)

        # Now a new user, Maria, comes along to the site.
        ## We use a new browser session to make sure that no
        ## information of Marcel is coming through from cookies etc.

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Maria starts a new list by entering a new item
        # The list is less interesting than Marcel's...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Buy milk')

        # Maria gets her own unique URL
        maria_list_url = self.browser.current_url
        self.assertRegex(marcel_list_url, '/lists/.+')
        self.assertNotEqual(marcel_list_url, maria_list_url)

        # Again, there is no trace of Marcel's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
