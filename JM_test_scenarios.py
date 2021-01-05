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
from JM_Elements_config import *


def test_01_HomePageToPersonalInsurance():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JMurl)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Personal_inurance_link)))
    assert driver.current_url == JMurl, 'Home Page Error'
    print('')
    print('Home Page Entered')
    driver.find_element_by_xpath(Personal_inurance_link).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Header_Personal_Insurance_elem)))
    print('Personal Insurance Page Entered')
    header_personal_insurance = driver.find_element_by_xpath(Header_Personal_Insurance_elem).text
    validation_box = driver.find_element_by_xpath(validation_box_elem).text
    time.sleep(2)
    print('Validating all elements of the Page')
    assert header_personal_insurance == Header_Personal_Insurance_config, "Expected header is".format(Header_Personal_Insurance_config)
    assert validation_box == validation_box_config, "Expected validation box is".format(validation_box_config)
    print('Validation Complete')
    # more asserts to add

