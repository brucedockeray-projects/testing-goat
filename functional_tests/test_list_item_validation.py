#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from django.test import LiveServerTestCase
from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    
    def test_cannot_add_empty_list_items(*self):
        pass
        # edit adds empty item to list
        
        # her entry is rejected with a message cannot add
        # empty item to list
        

