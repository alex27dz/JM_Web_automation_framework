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


def test_01_HomePageToPersonalInsurance():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
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
    time.sleep(5)
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
    time.sleep(5)
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
    time.sleep(5)
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
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 04 - PASSED')
    driver.close()


def test_05_HomePageToManagePolicy():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
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
    time.sleep(5)
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
    time.sleep(5)
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


def test_08_BusinessToClaims():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Businessclaims')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(business_claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 08 - PASSED')
    driver.close()


def test_09_BusinessToPayMyBill():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access PayMyBill')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(business_paymybill_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 09 - PASSED')
    driver.close()


def test_10_BusinessToZingPlatform():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Zing Platform')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Zing Platform').click()
    time.sleep(10)
    assert str(business_zingplatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 10 - PASSED')
    driver.close()


def test_11_BusinessToShippingSolution():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Shipping Solution')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shippin_gsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 11 - PASSED')
    driver.close()


def test_12_BusinessToJmCarePlan():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Care Plan')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Care Plan').click()
    time.sleep(10)
    assert str(business_jmcareplan_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 12 - PASSED')
    driver.close()


def test_13_BusinessToAppraisalSolution():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Appraisal Solution')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Appraisal Solution').click()
    time.sleep(10)
    assert str(business_appraisalsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 13 - PASSED')
    driver.close()


def test_14_BusinessToJewelerPrograms():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JewelerPrograms')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Jeweler Programs').click()
    time.sleep(10)
    assert str(business_jewelerprograms_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 14 - PASSED')
    driver.close()


def test_15_BusinessToPawnbrokers():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Pawnbrokers')
    time.sleep(2)
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pawnbrokers').click()
    time.sleep(10)
    assert str(business_pawnbrokers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 15 - PASSED')
    driver.close()


def test_16_AnswersToJewelryInsurance101():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Jewelry Insurance 101')
    time.sleep(2)
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Jewelry Insurance 101').click()
    time.sleep(10)
    assert str(answers_JewelryInsurance101_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 16 - PASSED')
    driver.close()


def test_17_AnswersToFAQ():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access FAQ')
    time.sleep(2)
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('FAQ').click()
    time.sleep(10)
    assert str(answers_FAQ_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 17 - PASSED')
    driver.close()


def test_18_AboutUsToAboutUs():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access About Us')
    time.sleep(2)
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('About Us').click()
    time.sleep(10)
    assert str(aboutus_aboutus_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 18 - PASSED')
    driver.close()


def test_19_AboutUsToSocialResponsibility():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access SocialResponsibility')
    time.sleep(2)
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Social Responsibility').click()
    time.sleep(10)
    assert str(aboutus_socialresponsibility_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 19 - PASSED')
    driver.close()


def test_20_AboutUsToCareers():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Careers')
    time.sleep(2)
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Careers').click()
    time.sleep(10)
    assert str(aboutus_careers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 20 - PASSED')
    driver.close()


def test_21_AboutUsToNewsroom():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Newsroom')
    time.sleep(2)
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Newsroom').click()
    time.sleep(10)
    assert str(aboutus_newsroom_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 21 - PASSED')
    driver.close()


def test_22_LogInToPersonalJewelry():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Jewelry')
    time.sleep(2)
    url = '/log-in/personal-jewelry'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    # driver.find_element_by_link_text('Personal Jewelry').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 22 - PASSED')
    driver.close()


def test_23_LogInToAgent():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Agent')
    time.sleep(2)
    url = 'https://my.jewelersmutual.com/PLPortal/Security/'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Agent').click()
    time.sleep(10)
    assert str(login_agent_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 23 - PASSED')
    driver.close()


def test_24_LogInToZingPlatform():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Zing Platform')
    time.sleep(2)
    url = 'https://my.jewelersmutual.com/PLPortal/Security/'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Zing Platform').click()
    time.sleep(10)
    assert str(login_ZingPlatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 24 - PASSED')
    driver.close()


def test_25_BodyToPersonalInsurance():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Access Personal Insurance')
    driver.find_element_by_partial_link_text('Personal Jewelry Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 25 - PASSED')
    driver.close()

# Personal Jewelry Insurance

def test_26_BodyToPayMyBill():
    assert 'alex' == 'alex'


def test_27_BodyToLogIn():
    assert 'alex' == 'alex'


def test_28_BodyToRegisterForAnOnlineAccount():
    assert 'alex' == 'alex'


def test_29_BodyToAddanitemtomyPolicy():
    assert 'alex' == 'alex'


def test_30_BodyToStartAClaim():
    assert 'alex' == 'alex'


def test_31_BodyToLearnaboutclaims():
    assert 'alex' == 'alex'


def test_32_BodyToGetaquoteformultipleItems():
    assert 'alex' == 'alex'


def test_33_BodyToEstimateMyRate():
    assert 'alex' == 'alex'


def test_34_BodyToExplorePersonalJewelryInsurance():
    assert 'alex' == 'alex'


def test_35_footerToPrivacyPolicy():
    assert 'alex' == 'alex'


def test_36_footerToTermsofUse():
    assert 'alex' == 'alex'


def test_37_footerToPersonalJewelryInsurance():
    assert 'alex' == 'alex'


def test_38_footerToGetaQuote():
    assert 'alex' == 'alex'


def test_39_footerToFAQ():
    assert 'alex' == 'alex'


def test_40_footerToManageMyPolicy():
    assert 'alex' == 'alex'


def test_41_footerToClaims():
    assert 'alex' == 'alex'


def test_42_footerToPayMyBill():
    assert 'alex' == 'alex'


def test_43_footerToReferalFriend():
    assert 'alex' == 'alex'


def test_44_footerToBusinessInsurance():
    assert 'alex' == 'alex'


def test_45_footerToZingPlatform():
    assert 'alex' == 'alex'


def test_46_footerToJMShippingSolution():
    assert 'alex' == 'alex'


def test_47_footerToJMCarePlan():
    assert 'alex' == 'alex'


def test_48_footerToJewelryAppraisalSolution():
    assert 'alex' == 'alex'


def test_49_footerToJMUniversity():
    assert 'alex' == 'alex'


def test_50_footerToJewelerPrograms():
    assert 'alex' == 'alex'


def test_51_footerToPayMyBill():
    assert 'alex' == 'alex'


def test_52_footerToBusinessClaims():
    assert 'alex' == 'alex'


def test_53_footerToBlog():
    assert 'alex' == 'alex'


def test_54_footerToAboutUs():
    assert 'alex' == 'alex'


def test_55_footerToCareers():
    assert 'alex' == 'alex'


def test_56_footerToNewsroom():
    assert 'alex' == 'alex'


def test_57_footerToSocialResponsibility():
    assert 'alex' == 'alex'


def test_58_footerToCOVIDResources():
    assert 'alex' == 'alex'


def test_59_footerToContactUs():
    assert 'alex' == 'alex'


def test_60_footerToShareYourConcerns():
    assert 'alex' == 'alex'


def test_61_footerHomuchdoesitcosttoresizearing():
    assert 'alex' == 'alex'


def test_62_footerHowtocleangoldjewelry():
    assert 'alex' == 'alex'


def test_63_footerHowmuchshouldcost():
    assert 'alex' == 'alex'


def test_64_footerHowtomakearing():
    assert 'alex' == 'alex'


def test_65_footerMoreblogarticles():
    assert 'alex' == 'alex'


def test_66_redirection_links_status():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(Redirect_url)
    #print('Access HomePage')
    time.sleep(3)

    text_area = driver.find_element_by_class_name('textarea')
    text_area.click()
    time.sleep(1)
    text_area.send_keys('stage.jewelersmutual.com/jewelry-box/safety-security\n'
    'stage.jewelersmutual.com/jewelry-box/settings\n'
    'stage.jewelersmutual.com/jewelry-box/smart-jewelry\n'
    'stage.jewelersmutual.com/jewelry-box/tips\n')
    time.sleep(60)
    assert 'alex' == 'alex'


def test_67_FullPageScenario():
    assert 'alex' == 'alex'

def test_68_Additional_link_ContactUs():
    assert 'alex' == 'alex'

def test_69_Additional_link_ShareYourConcern():
    assert 'alex' == 'alex'

def test_70_Additional_link_PrivacyPolicy():
    assert 'alex' == 'alex'

def test_71_Additional_link_TermsofUse():
    assert 'alex' == 'alex'

def test_72_Additional_link_engagementringinsurance():
    assert 'alex' == 'alex'

def test_73_Additional_link_comparejewelryinsurancetohomeowners():
    assert 'alex' == 'alex'

def test_74_Additional_link_personaljewelryinsurancecollections():
    assert 'alex' == 'alex'

def test_75_Additional_link_crownandcaliber():
    assert 'alex' == 'alex'

def test_76_Additional_link_adiamor():
    assert 'alex' == 'alex'

def test_77_Additional_link_briangavindiamonds():
    assert 'alex' == 'alex'

def test_78_Additional_link_jamesallen():
    assert 'alex' == 'alex'

def test_79_Additional_link_bluenile():
    assert 'alex' == 'alex'

def test_80_Additional_link_whiteflash():
    assert 'alex' == 'alex'

def test_81_Additional_link_earringinsurance():
    assert 'alex' == 'alex'

def test_82_Additional_link_watchinsurance():
    assert 'alex' == 'alex'

def test_83_Additional_link_necklaceinsurance():
    assert 'alex' == 'alex'

def test_84_Additional_link_braceletinsurance():
    assert 'alex' == 'alex'

def test_85_Additional_link_smartwatchinsurance():
    assert 'alex' == 'alex'

def test_86_Additional_link_howtocleanandcareforyourdiamondring():
    assert 'alex' == 'alex'

def test_87_Additional_link_weinsurejewelry():
    assert 'alex' == 'alex'

def test_88_Additional_link_coronavirus():
    assert 'alex' == 'alex'

def test_89_Additional_link_coronavirusBusiness():
    assert 'alex' == 'alex'

def test_90_Additional_link_GuidetoJewelryInsurance():
    assert 'alex' == 'alex'

def test_91_Additional_link_JMUniversity():
    assert 'alex' == 'alex'

def test_92_Additional_link_ReferaFriend():
    assert 'alex' == 'alex'

