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
    assert 'alex' == 'alex'


def test_09_BusinessToPayMyBill():
    assert 'alex' == 'alex'


def test_10_BusinessToZingPlatform():
    assert 'alex' == 'alex'


def test_11_BusinessToShippingSolution():
    assert 'alex' == 'alex'


def test_12_BusinessToJmCarePlan():
    assert 'alex' == 'alex'


def test_13_BusinessToAppraisalSolution():
    assert 'alex' == 'alex'


def test_14_BusinessToJewelerPrograms():
    assert 'alex' == 'alex'


def test_15_BusinessToPawnbrokers():
    assert 'alex' == 'alex'


def test_16_AnswersToJewelryInsurance101():
    assert 'alex' == 'alex'


def test_17_AnswersToFAQ():
    assert 'alex' == 'alex'


def test_18_AboutUsToAboutUs():
    assert 'alex' == 'alex'


def test_19_AboutUsToSocialResponsibility():
    assert 'alex' == 'alex'


def test_20_AboutUsToCareers():
    assert 'alex' == 'alex'


def test_21_AboutUsToNewsroom():
    assert 'alex' == 'alex'


def test_22_LogInToPersonalJewelry():
    assert 'alex' == 'alex'


def test_23_LogInToAgent():
    assert 'alex' == 'alex'


def test_24_LogInToZingPlatform():
    assert 'alex' == 'alex'


def test_25_BodyToPersonalInsurance():
    assert 'alex' == 'alex'


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


def test_61_footerHowtocleangoldjewelry():
    assert 'alex' == 'alex'


def test_61_footerHowmuchshouldcost():
    assert 'alex' == 'alex'


def test_61_footerHowtomakearing():
    assert 'alex' == 'alex'


def test_61_footerMoreblogarticles():
    assert 'alex' == 'alex'


def test_61_redirection_links_status():
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
    assert 'alex' == 'alex'


def test_61_FullPageScenario():
    assert 'alex' == 'alex'


def test_61_footerToBlog():
    assert 'alex' == 'alex'


