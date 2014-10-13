from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import LiveServerTestCase
from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    
    def test_cannot_add_empty_list_items(self):
        
        # user adds empty item to list
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        # the page refereshes and her entry is rejected with a message cannot add
        # empty item to list
        error=self.browser.find_element_by_css_selector('._has_error')
        self.assertEqual(error.text,"You can't have an empty list item")
        
        # the user tries again , this time the entry has text so it should work
        self.browser.find_element_by_id('id_new_item').send_keys('Physio needed\n')
        self.check_for_row_in_list_table('1: Physio neeeded')
        
        # now user tries to add a second blank item !
        self.browser.find_element-by_id('id_new_item').send_keys('\n')
        
        # user receives the warning again
        self.check_for_row_in_list_table('1: Physio neeeded')
        error=self.browser.find_element_by_css_selector('._has_error')
        self.assertEqual(error.text,"You can't have an empty list item")
        
        # error can be corected by again filing in some text
        self.browser.find_element_by_id('id_new_item').send_keys('Take paracetemol\n')
        self.check_for_row_in_list_table('1: Physio neeeded')
        self.check_for_row_in_list_table('1: Take paracetemol')

