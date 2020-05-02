"""
Functional Test corresponds to the user story.
"""

from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app.
# She goes to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists

assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

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
browser.quit()
