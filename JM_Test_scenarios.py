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


# def test_00_redirection_links_status():
#     driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
#     driver.get(Redirect_url)
#     #print('Access HomePage')
#     time.sleep(3)
#
#     text_area = driver.find_element_by_class_name('textarea')
#     text_area.click()
#     time.sleep(1)
#     text_area.send_keys('stage.jewelersmutual.com/jewelry-box/safety-security\n'
#     'stage.jewelersmutual.com/jewelry-box/settings\n'
#     'stage.jewelersmutual.com/jewelry-box/smart-jewelry\n'
#     'stage.jewelersmutual.com/jewelry-box/tips\n')
#     time.sleep(60)


def test_01_HomePageToPersonalInsurance():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Insurance')
    time.sleep(2)
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Personal Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 01 - PASSED')
    driver.close()


def test_02_HomePageToGetaQuote():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access GetaQuote')
    time.sleep(2)
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Get a Quote').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of Get a Quote - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 02 - PASSED')
    driver.close()


def test_03_HomePageToPayMyBill():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access PayMyBill')
    time.sleep(2)
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 03 - PASSED')
    driver.close()

def test_04_HomePageToClaims():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Claims')
    time.sleep(2)
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 04 - PASSED')
    driver.close()


def test_05_HomePageToManagePolicy():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Manage my policy')
    time.sleep(2)
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Manage My Policy').click()
    time.sleep(10)
    assert str(manage_my_policy_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 05 - PASSED')
    driver.close()

def test_06_HomePageToBlog():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Blog')
    time.sleep(2)
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Blog').click()
    time.sleep(10)
    assert str(blog_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 06 - PASSED')
    driver.close()


def test_07_BusinessToBusinessInsurance():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(3)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access BusinessInsurance')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Business Insurance').click()
    time.sleep(10)
    assert str(business_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 07 - PASSED')
    driver.close()


# stopped on copying JM Shipping Solution elements names






# 	And I select the business:claims on homepage
# 	#Then I Verify all the elements in the Pawn Brokers page are displayed
# 	And I navigate back to the home page
# 	And I select the business:pay my bill on homepage
# 	#Then I Verify all the elements in the Pawn Brokers page are displayed
# 	And I navigate back to the home page
# 	And I select the business:zing platform on homepage
# 	#Then I Verify all the elements in the Pawn Brokers page are displayed
# 	And I navigate back to the home page
# 	And I select the business:shipping solution on homepage
# 	Then I Verify all the elements in the Shipping solution page are displayed
# 	And I navigate back to the home page
# 	And I select the business:jm care plan on homepage
# 	#Then I Verify all the elements in the Pawn Brokers page are displayed
# 	And I navigate back to the home page
# 	And I select the business:jeweler programs on homepage
# 	Then I Verify all the elements in the Jeweler Programs page are displayed
# 	And I navigate back to the home page
# 	And I select the business:pawnbrokers on homepage
# 	Then I Verify all the elements in the Pawn Brokers page are displayed
# 	And I navigate back to the home page
#
# 	# about us
# 	And I select the about us:newsroom on homepage
# 	#Then I Verify all the elements in the Careers page are displayed
# 	And I navigate back to the home page
# 	And I select the about us:about us on homepage
# 	Then I Verify all the elements in the about us page are displayed
# 	And I navigate back to the home page
# 	And I select the about us:social responsibility on homepage
# 	Then I Verify all the elements in the SocialResponsibility page are displayed
# 	And I navigate back to the home page
# 	And I select the about us:careers on homepage
# 	Then I Verify all the elements in the Careers page are displayed
# 	And I navigate back to the home page


# 	And I select the answers:faq on homepage
# 	#Then I Verify all the elements in the Pawn Brokers page are displayed
# 	And I navigate back to the home page
# 	# And I select the answers:jewelry insurance 101 on homepage
# 	# Then I Verify all the elements in the Pawn Brokers page are displayed
# 	# And I navigate back to the home page
#
# # log in
# 	And I select the login:personal jewelry on homepage
# 	Then I Verify all the elements in the ManageMyPolicy page are displayed
# 	And I navigate back to the home page
# 	And I select the login:zing platform on homepage
# 	#Then I Verify all the elements in the Agent Portal page are displayed
# 	And I navigate back to the home page
# 	And I select the login:agent on homepage
# 	Then I Verify all the elements in the Agent Portal page are displayed
# 	And I navigate back to the home page
#
# # footer
# 	And I select the contact on homepage
# 	Then I Verify all the elements in the Contact page are displayed
# 	And I navigate back to the home page
# 	And I select the privacy policy on homepage
# 	Then I Verify all the elements in the privacy policy page are displayed
# 	And I navigate back to the home page
# 	And I select the terms of use on homepage
# 	Then I Verify all the elements in the terms of use page are displayed
# 	And I navigate back to the home page
# 	And I select the share your concerns on homepage
# 	Then I Verify all the elements in the share your concerns page are displayed
# 	And I navigate back to the home page
# 	And I select the careers on homepage
# 	Then I Verify all the elements in the Careers page are displayed
# 	And I navigate back to the home page
# 	And I select the newsroom on homepage
# 	Then I Verify all the elements in the Newsroom page are displayed
# 	And I navigate back to the home page
# 	And I select the explore personal jewelry insurance on homepage
# 	# Then I Verify all the elements in the Newsroom page are displayed
# 	And I navigate back to the home page
# 	And I select the trust:explore personal jewelry insurance on homepage
# 	# Then I Verify all the elements in the Newsroom page are displayed
# 	Then I navigate back to the home page
#
#
# Examples:
# 	| Test Case #   | applicationType | target  | browser | Capability |
# 	| HomePageLinks | DRUPAL          | Desktop | Chrome  | IPhoneX    |
#


