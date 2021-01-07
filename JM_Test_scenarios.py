import requests
import json
import time
import pprint
import logging
import mysql.connector
import datetime
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import json  # working with json dicts
import yagmail  # importing all email file to use send function
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl.styles import Alignment
import urllib.request
import pytest
from selenium import webdriver
from JM_Generic_functions import *


# Body - different for every link
# header_personal_insurance = driver.find_element_by_xpath(Header_Personal_Insurance_elem).text
# validation_box = driver.find_element_by_xpath(validation_box_elem).text
#
# print('Validating all elements of the Page')
# assert header_personal_insurance == Header_Personal_Insurance_config, "Expected header is".format(Header_Personal_Insurance_config)
# assert validation_box == validation_box_config, "Expected validation box is".format(validation_box_config)


def test_01_HomePageToPersonalInsurance():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('I access HomePage')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'

    print('Personal Insurance')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'







