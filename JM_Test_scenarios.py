import requests
import json
import time
import pprint
import logging
# import mysql.connector
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

# Drivers location
# chrome_location = 'C:/ChromeDriver/chromedriver'
chrome_location = "/Users/alexdezho/Downloads/chromedriver"
ie_location = ""
edge_location = ""
firefox_location = ""
driver_location = chrome_location
tag = 'Chrome'
# driver_location = ie_location
# tag = 'IE'
# driver_location = edge_location
# tag = 'Edge'
# driver_location = firefox_location
# tag = 'Firefox'

# urls
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"

def test_01_HomePageToPersonalInsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Insurance')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access GetaQuote')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access PayMyBill')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Claims')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Manage my policy')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Blog')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access BusinessInsurance')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Businessclaims')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access PayMyBill')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Zing Platform')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Shipping Solution')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shipping_solution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 11 - PASSED')
    driver.close()


def test_12_BusinessToJmCarePlan():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Care Plan')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Appraisal Solution')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JewelerPrograms')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Pawnbrokers')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Jewelry Insurance 101')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access FAQ')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access About Us')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access SocialResponsibility')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Careers')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Newsroom')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Jewelry')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Personal Jewelry').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 22 - PASSED')
    driver.close()


def test_22_LogInToPersonalJewelry():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Jewelry')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Personal Jewelry').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 22 - PASSED')
    driver.close()


def test_23_LogInToAgent():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Agent')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Zing Platform')
    url = 'https://my.testjewelersmutual.com/plportal'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    print('Access Personal Insurance')
    driver.find_element_by_partial_link_text('EXPLORE PERSONAL JEWELRY INSURANCE').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 25 - PASSED')
    driver.close()


def test_26_BodyToLogIn():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Log in')
    driver.find_element_by_partial_link_text('Log in').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 26 - PASSED')
    driver.close()


def test_27_BodyToRegisterForAnOnlineAccount():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access BodyToRegisterForAnOnlineAccount')
    driver.find_element_by_partial_link_text('Register for an online account').click()
    # stopped here
    time.sleep(10)
    assert str(body_ToRegisterForAnOnlineAccount(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 27 - PASSED')
    driver.close()


def test_28_BodyToAddanitemtomyPolicy():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Add an item to my policy')
    driver.find_element_by_partial_link_text('Add an item to my policy').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 28 - PASSED')
    driver.close()


def test_29_BodyTopaymybill():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Pay My Bill')
    driver.find_element_by_partial_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 29 - PASSED')
    driver.close()


def test_30_BodyToStartAClaim():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Start a claim')
    driver.find_element_by_partial_link_text('Start a claim').click()
    time.sleep(10)
    assert str(body_startaclaim(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 30 - PASSED')
    driver.close()


def test_31_BodyToLearnaboutclaims():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Learn about claims')
    driver.find_element_by_partial_link_text('Learn about claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 31 - PASSED')
    driver.close()


def test_32_BodyToGetaquoteformultipleItems():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(3)
    print('Get a quote for multiple items')
    driver.find_element_by_partial_link_text('Get a quote for multiple items').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 32 - PASSED')
    driver.close()


def test_33_BodyToExplorePersonalJewelryInsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep(3)
    print('EXPLORE PERSONAL JEWELRY INSURANCE')
    driver.find_element_by_partial_link_text('EXPLORE PERSONAL JEWELRY INSURANCE').click()
    time.sleep(10)
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 33 - PASSED')
    driver.close()


def test_34_footerToPersonalJewelryInsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Personal Jewelry Insurance')
    driver.find_element_by_link_text('Personal Jewelry Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 34 - PASSED')
    driver.close()


def test_35_footerToGetaQuote():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Get a Quote')
    driver.find_element_by_link_text('Get a Quote').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of Get a Quote - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 35 - PASSED')
    driver.close()


def test_36_footerToFAQ():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('FAQ')
    driver.find_element_by_link_text('FAQ').click()
    time.sleep(10)
    assert str(answers_FAQ_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 36 - PASSED')
    driver.close()


def test_37_footerToManageMyPolicy():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Manage My Policy')
    driver.find_element_by_link_text('Manage My Policy').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 37 - PASSED')
    driver.close()


def test_38_footerToClaims():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Claims')
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 38 - PASSED')
    driver.close()


def test_39_footerToPayMyBill():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Pay My Bill')
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 39 - PASSED')
    driver.close()


def test_40_footerToBusinessInsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jewelry Business Insurance')
    driver.find_element_by_link_text('Jewelry Business Insurance').click()
    time.sleep(10)
    assert str(business_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 40 - PASSED')
    driver.close()


def test_41_footerToZingPlatform():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Zing® Platform')
    driver.find_element_by_link_text('Zing® Platform').click()
    time.sleep(10)
    assert str(business_zingplatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 41 - PASSED')
    driver.close()


def test_42_footerToJMShippingSolution():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ Shipping Solution')
    driver.find_element_by_link_text('JM™ Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shipping_solution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 42 - PASSED')
    driver.close()


def test_43_footerToJMCarePlan():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ Care Plan')
    driver.find_element_by_link_text('JM™ Care Plan').click()
    time.sleep(10)
    assert str(business_jmcareplan_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 43 - PASSED')
    driver.close()


def test_44_footerToJewelryAppraisalSolution():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jewelry Appraisal Solution')
    driver.find_element_by_link_text('Jewelry Appraisal Solution').click()
    time.sleep(10)
    assert str(business_appraisalsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 44 - PASSED')
    driver.close()


def test_45_footerToJMUniversity():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ University')
    driver.find_element_by_link_text('JM™ University').click()
    time.sleep(10)
    assert str(body_jmuniversity(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 45 - PASSED')
    driver.close()


def test_46_footerToJewelerPrograms():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jeweler Programs')
    driver.find_element_by_link_text('Jeweler Programs').click()
    time.sleep(10)
    assert str(business_jewelerprograms_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 46 - PASSED')
    driver.close()


def test_47_footerToPayMyBill():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Pay My Bill')
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(business_paymybill_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 47 - PASSED')
    driver.close()


def test_48_footerToBusinessClaims():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Business Claims')
    driver.find_element_by_link_text('Business Claims').click()
    time.sleep(10)
    assert str(business_claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 48 - PASSED')
    driver.close()


def test_49_footerToBlog():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Blog')
    driver.find_element_by_link_text('Blog').click()
    time.sleep(10)
    assert str(blog_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 49 - PASSED')
    driver.close()


def test_50_footerToAboutUs():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('About Us')
    driver.find_element_by_link_text('About Us').click()
    time.sleep(10)
    assert str(aboutus_aboutus_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 50 - PASSED')
    driver.close()


def test_51_footerToCareers():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Careers')
    driver.find_element_by_link_text('Careers').click()
    time.sleep(10)
    assert str(aboutus_careers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 51 - PASSED')
    driver.close()


def test_52_footerToNewsroom():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Newsroom')
    driver.find_element_by_link_text('Newsroom').click()
    time.sleep(10)
    assert str(aboutus_newsroom_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 52 - PASSED')
    driver.close()


def test_53_footerToSocialResponsibility():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Social Responsibility')
    driver.find_element_by_link_text('Social Responsibility').click()
    time.sleep(10)
    assert str(aboutus_socialresponsibility_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 53 - PASSED')
    driver.close()


def test_54_footerToCOVIDResources():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('COVID-19 Resources')
    driver.find_element_by_link_text('COVID-19 Resources').click()
    time.sleep(10)
    assert str(body_COVIDResources(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 54 - PASSED')
    driver.close()


def test_55_footerToContactUs():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Contact Us')
    driver.find_element_by_link_text('Contact Us').click()
    time.sleep(10)
    assert str(body_ContactUs(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 55 - PASSED')
    driver.close()


def test_56_footerToShareYourConcerns():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Share Your Concerns')
    driver.find_element_by_link_text('Share Your Concerns').click()
    time.sleep(10)
    assert str(body_ShareYourConcerns(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 56 - PASSED')
    driver.close()


def test_57_footerHomuchdoesitcosttoresizearing():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How much does it cost to resize a ring?')
    driver.find_element_by_link_text('How much does it cost to resize a ring?').click()
    time.sleep(10)
    assert str(body_Homuchdoesitcosttoresizearing(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 57 - PASSED')
    driver.close()


def test_58_footerHowtocleangoldjewelry():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How to clean gold jewelry the right way')
    driver.find_element_by_link_text('How to clean gold jewelry the right way').click()
    time.sleep(10)
    assert str(body_Howtocleangoldjewelry(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 58 - PASSED')
    driver.close()


def test_59_footerHowmuchshouldcost():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How much should an appraisal cost?')
    driver.find_element_by_link_text('How much should an appraisal cost?').click()
    time.sleep(10)
    assert str(body_Howmuchshouldcost(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 59 - PASSED')
    driver.close()


def test_60_footerHowtomakearing():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How to make a ring smaller without resizing')
    driver.find_element_by_link_text('How to make a ring smaller without resizing').click()
    time.sleep(10)
    assert str(body_Howtomakearing(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 60 - PASSED')
    driver.close()


def test_61_footerMoreblogarticles():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('More blog articles')
    driver.find_element_by_link_text('More blog articles').click()
    time.sleep(10)
    assert str(body_Moreblogarticles(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 61 - PASSED')
    driver.close()


def test_62_footerToPrivacyPolicy():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Privacy Policy')
    driver.find_element_by_link_text('Privacy Policy').click()
    time.sleep(10)
    assert str(body_PrivacyPolicy(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 62 - PASSED')
    driver.close()


def test_63_footerToTermsofUse():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    time.sleep(2)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Terms of Use')
    driver.find_element_by_link_text('Terms of Use').click()
    time.sleep(10)
    assert str(body_TermsofUse(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 63 - PASSED')
    driver.close()


def test_66_Additional_link_engagementringinsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("")
    driver.get('https://www.jewelersmutual.com/engagement-ring-insurance')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_engagementringinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 66 - PASSED')
    driver.close()


def test_67_Additional_link_comparejewelryinsurancetohomeowners():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/compare-jewelry-insurance-to-homeowners')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_comparejewelryinsurancetohomeowners(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 67 - PASSED')
    driver.close()


def test_68_Additional_link_personaljewelryinsurancecollections():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/personal-jewelry-insurance-collections')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_personaljewelryinsurancecollections(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 68 - PASSED')
    driver.close()


def test_69_Additional_link_crownandcaliber():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/crownandcaliber')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_crownandcaliber(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 69 - PASSED')
    driver.close()


def test_70_Additional_link_adiamor():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/adiamor')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_adiamor(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 70 - PASSED')
    driver.close()


def test_71_Additional_link_briangavindiamonds():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/briangavindiamonds')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_briangavindiamonds(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 71 - PASSED')
    driver.close()


def test_72_Additional_link_jamesallen():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/jamesallen')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_jamesallen(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 72 - PASSED')
    driver.close()


def test_73_Additional_link_bluenile():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/bluenile')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_bluenile(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 73 - PASSED')
    driver.close()


def test_74_Additional_link_whiteflash():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/whiteflash')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_whiteflash(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 74 - PASSED')
    driver.close()


def test_75_Additional_link_earringinsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/earring-insurance')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_earringinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 75 - PASSED')
    driver.close()


def test_76_Additional_link_watchinsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/watch-insurance')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_watchinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 76 - PASSED')
    driver.close()


def test_77_Additional_link_necklaceinsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/necklace-insurance')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_necklaceinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 77 - PASSED')
    driver.close()


def test_78_Additional_link_braceletinsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/bracelet-insurance')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_braceletinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 78 - PASSED')
    driver.close()


def test_79_Additional_link_smartwatchinsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/smartwatch-insurance')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_smartwatchinsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 79 - PASSED')
    driver.close()


def test_80_Additional_link_howtocleanandcareforyourdiamondring():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/how-to-clean-and-care-for-your-diamond-ring')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_howtocleanandcareforyourdiamondring(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 80 - PASSED')
    driver.close()


def test_81_Additional_link_weinsurejewelry():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/we-insure-jewelry')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_weinsurejewelry(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 81 - PASSED')
    driver.close()


def test_82_Additional_link_coronavirusBusiness():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/coronavirus-businesses')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_coronavirusBusiness(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 82 - PASSED')
    driver.close()


def test_83_Additional_link_GuidetoJewelryInsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE
        driver = webdriver.Ie("JM-machine location")
    driver.get('https://www.jewelersmutual.com/jewelry-insurance-guide')
    driver.fullscreen_window()
    time.sleep(10)
    assert str(body_GuidetoJewelryInsurance(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 83 - PASSED')
    driver.close()


def test_84_embedded_quote():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    driver.fullscreen_window()
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,1000)")
    time.sleep(15)
    driver.find_element_by_id('itemType').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="itemType"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_id('replacement_value').click()
    time.sleep(2)
    driver.find_element_by_id('replacement_value').send_keys('200')
    time.sleep(2)
    driver.find_element_by_id('postalCode').click()
    time.sleep(2)
    driver.find_element_by_id('postalCode').send_keys('53189')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="step1"]/form/div[4]/div/button').click()
    driver.find_element_by_xpath('//*[@id="step1"]/form/div[4]/div/button').click()
    time.sleep(5)
    assert str(embedded_quote_Estimatemyrate(driver)) == 'True', 'Navbar elements - not found'
    time.sleep(2)
    print('SCENARIO - 85 - PASSED')
    driver.close()

# unfinished scenarios
# def test_85_homepage():
#     if tag == 'Chrome':
#         driver = webdriver.Chrome(driver_location)
#     else:  # IE
#         driver = webdriver.Ie("JM-machine location")
#     driver.get(JM_url)
#     driver.fullscreen_window()
#     print('Access HomePage')
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
#     print('verify navbar and footer')
#     assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
#     assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
#     assert str(body_homepage(driver)) == 'True', 'Footer elements - not found'
#     time.sleep(3)
#     print('SCENARIO - 84 - PASSED')
#     driver.close()




# def test_64_FullPageScenario():
#     if tag == 'Chrome':
#         driver = webdriver.Chrome(driver_location)
#     else:  # IE
#         driver = webdriver.Ie("JM-machine location")
#     driver.get(JM_url)
#     print('Access HomePage')
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
#     print('verify navbar and footer')
#     assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
#     assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
#     driver.execute_script("window.scrollTo(0,0)")
#
#     print('Full scenario passed')
# def test_65_redirection_links_status():
    # driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    # driver.get(Redirect_url)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
    # text_area = driver.find_element_by_class_name('textarea')
    # text_area.click()
    # time.sleep(2)
    # text_area.send_keys('stage.jewelersmutual.com/earrings\n'
    # 'stage.jewelersmutual.com/engagement\n'
    # 'stage.jewelersmutual.com/gems\n'
    # 'stage.jewelersmutual.com/holidays\n'
    # 'stage.jewelersmutual.com/necklaces\n'
    # 'stage.jewelersmutual.com/proposal\n'
    # 'stage.jewelersmutual.com/rings\n'
    # 'stage.jewelersmutual.com/safety-security\n'
    # 'stage.jewelersmutual.com/settings\n'
    # 'stage.jewelersmutual.com/tips\n'
    # 'stage.jewelersmutual.com/trends\n'
    # 'stage.jewelersmutual.com/watches\n'
    # 'stage.jewelersmutual.com/wedding\n'
    # 'stage.jewelersmutual.com/jewelry-box\n'
    # 'stage.jewelersmutual.com/jewelry-box/anniversary\n'
    # 'stage.jewelersmutual.com/jewelry-box/appraisal\n'
    # 'stage.jewelersmutual.com/jewelry-box/bracelets\n'
    # 'stage.jewelersmutual.com/jewelry-box/brooch\n'
    # 'stage.jewelersmutual.com/jewelry-box/claims\n'
    # 'stage.jewelersmutual.com/jewelry-box/cleaning-care\n'
    # 'stage.jewelersmutual.com/jewelry-box/contests-promotions\n'
    # 'stage.jewelersmutual.com/jewelry-box/coverage\n'
    # 'stage.jewelersmutual.com/jewelry-box/customer-service\n'
    # 'stage.jewelersmutual.com/jewelry-box/earrings\n'
    # 'stage.jewelersmutual.com/jewelry-box/engagement\n'
    # 'stage.jewelersmutual.com/jewelry-box/gems\n'
    # 'stage.jewelersmutual.com/jewelry-box/holidays\n'
    # 'stage.jewelersmutual.com/jewelry-box/necklaces\n'
    # 'stage.jewelersmutual.com/jewelry-box/proposal\n'
    # 'stage.jewelersmutual.com/jewelry-box/rings\n'
    # 'stage.jewelersmutual.com/jewelry-box/safety-security\n'
    # 'stage.jewelersmutual.com/jewelry-box/settings\n'
    # 'stage.jewelersmutual.com/jewelry-box/smart-jewelry\n'
    # 'stage.jewelersmutual.com/jewelry-box/tips\n'
    # 'stage.jewelersmutual.com/jewelry-box/travel\n'
    # 'stage.jewelersmutual.com/jewelry-box/trends\n'
    # 'stage.jewelersmutual.com/jewelry-box/watches\n'
    # 'stage.jewelersmutual.com/jewelry-box/wedding\n'
    # 'stage.jewelersmutual.com/Business/Blog-CL\n'
    # 'stage.jewelersmutual.com/Business/Pay-My-Bill\n'
    # 'stage.jewelersmutual.com/Our-Story\n'
    # 'stage.jewelersmutual.com/Personal/Blog-PL\n'
    # 'stage.jewelersmutual.com/Personal/Claims/Start-A-Claim\n'
    # 'stage.jewelersmutual.com/Personal/Get-a-Quote\n'
    # 'stage.jewelersmutual.com/Personal/Manage-My-Policy\n'
    # 'stage.jewelersmutual.com/Personal/Pay-My-Bill\n'
    # 'stage.jewelersmutual.com/Personal/Personal-Insurance\n'
    # 'stage.jewelersmutual.com/quote\n'
    # 'stage.jewelersmutual.com/Redirects/Retrieve\n'
    # 'stage.jewelersmutual.com/Business/JM-University\n'
    # 'stage.jewelersmutual.com/Log-In/Agent\n'
    # 'stage.jewelersmutual.com/Log-In/Personal-Jewelry\n'
    # 'stage.jewelersmutual.com/Pawn\n'
    # 'stage.jewelersmutual.com/payonline\n'
    # 'stage.jewelersmutual.com/protectallurez\n'
    # 'stage.jewelersmutual.com/protectbestbrilliance\n'
    # 'stage.jewelersmutual.com/protectbluechipjewelry\n'
    # 'stage.jewelersmutual.com/protectcrownandcaliber\n'
    # 'stage.jewelersmutual.com/protectdanielsjewelers\n'
    # 'stage.jewelersmutual.com/Redirects/addjewelry\n'
    # 'stage.jewelersmutual.com/Redirects/Upload/Appraisal\n'
    # 'stage.jewelersmutual.com/protectderco\n'
    # 'stage.jewelersmutual.com/protectgemprint\n'
    # 'stage.jewelersmutual.com/protecthemmingjewelers\n'
    # 'stage.jewelersmutual.com/protecthydepark\n'
    # 'stage.jewelersmutual.com/protectintergem\n'
    # 'stage.jewelersmutual.com/protectjosephschubach\n'
    # 'stage.jewelersmutual.com/protectloverly\n'
    # 'stage.jewelersmutual.com/protectmsimagines\n'
    # 'stage.jewelersmutual.com/protectmydiamond\n'
    # 'stage.jewelersmutual.com/protectportion\n'
    # 'stage.jewelersmutual.com/protectprestigetimellc\n'
    # 'stage.jewelersmutual.com/Affluent-Insurance\n'
    # 'stage.jewelersmutual.com/protectpricescope\n'
    # 'stage.jewelersmutual.com/protectraleighdiamond\n'
    # 'stage.jewelersmutual.com/protectrockher\n'
    # 'stage.jewelersmutual.com/protectstevensinger\n'
    # 'stage.jewelersmutual.com/protecttaylorandhart\n'
    # 'stage.jewelersmutual.com/protecttruefacet\n'
    # 'stage.jewelersmutual.com/protecttrumpetandhorn\n'
    # 'stage.jewelersmutual.com/protectvenaamors\n'
    # 'stage.jewelersmutual.com/protectwatchfacts\n'
    # 'stage.jewelersmutual.com/protectzoara\n'
    # 'stage.jewelersmutual.com/buyersguide\n'
    # 'stage.jewelersmutual.com/claims\n'
    # 'stage.jewelersmutual.com/Log-In/Business-Owner\n'
    # 'stage.jewelersmutual.com/opensourcejewelry\n'
    # 'stage.jewelersmutual.com/Personal/Register-PL\n'
    # 'stage.jewelersmutual.com/PLPortal\n'
    # 'stage.jewelersmutual.com/protectdctaylorjewellers\n'
    # 'stage.jewelersmutual.com/protectheartsonfire\n'
    # 'stage.jewelersmutual.com/protectjewellerybysanders\n'
    # 'stage.jewelersmutual.com/protectmytiffany\n'
    # 'stage.jewelersmutual.com/protectringwraps\n'
    # 'stage.jewelersmutual.com/protecttacori\n'
    # 'stage.jewelersmutual.com/protectvraiandoro\n'
    # 'stage.jewelersmutual.com/protectwatchmaxx\n'
    # 'stage.jewelersmutual.com/protectwindycitydiamonds\n'
    # 'stage.jewelersmutual.com/protectasdgemsllc\n')
    # time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section[2]/div/form/div[2]/div/a').click()
    # time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]').click()
    # time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]/span[1]/select/optgroup/option[4]').click()
    # time.sleep(5)
    # if driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]').click():
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]/select/optgroup/option[3]').click()
    #     time.sleep(10)
    #     errors = driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text
    #     print(driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text)
    #     driver.back()
    #     assert errors == '0 URLs', '404 status in redirection links'
    # else:
    #     driver.back()
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
    #     text_area = driver.find_element_by_class_name('textarea')
    #     text_area.click()
    #     text_area.click()
    #     time.sleep(2)
    #     text_area.send_keys('stage.jewelersmutual.com/protectbarclaysjewellers\n'
    #     'stage.jewelersmutual.com/protectdavidyurman\n'
    #     'stage.jewelersmutual.com/protectdiamondfoundry\n'
    #     'stage.jewelersmutual.com/protectdiamondneed\n'
    #     'stage.jewelersmutual.com/protectkenanddanadesign\n'
    #     'stage.jewelersmutual.com/protectpeterindorf\n'
    #     'stage.jewelersmutual.com/protectschmittjewelers\n'
    #     'stage.jewelersmutual.com/protecttourneau\n'
    #     'stage.jewelersmutual.com/protectveleskajewelry\n'
    #     'stage.jewelersmutual.com/Complaint-Resolution-Process\n'
    #     'stage.jewelersmutual.com/About/Careers\n'
    #     'stage.jewelersmutual.com/Affluent-Insurance\n'
    #     'stage.jewelersmutual.com/appraisal\n'
    #     'stage.jewelersmutual.com/appraisalupload\n'
    #     'stage.jewelersmutual.com/bandtogether\n'
    #     'stage.jewelersmutual.com/bday\n'
    #     'stage.jewelersmutual.com/Benefits\n'
    #     'stage.jewelersmutual.com/Business/Blog-CL\n'
    #     'stage.jewelersmutual.com/Business/JM-University\n'
    #     'stage.jewelersmutual.com/buyersguide\n'
    #     'stage.jewelersmutual.com/Careers\n'
    #     'stage.jewelersmutual.com/careguide\n'
    #     'stage.jewelersmutual.com/consumer\n'
    #     'stage.jewelersmutual.com/diamondcare\n'
    #     'stage.jewelersmutual.com/freequote\n'
    #     'stage.jewelersmutual.com/hemi\n'
    #     'stage.jewelersmutual.com/homerun\n'
    #     'stage.jewelersmutual.com/ja\n'
    #     'stage.jewelersmutual.com/Our-Story\n'
    #     'stage.jewelersmutual.com/Pawn\n'
    #     'stage.jewelersmutual.com/Personal/Blog-PL\n'
    #     'stage.jewelersmutual.com/Personal/Personal-Insurance\n'
    #     'stage.jewelersmutual.com/protect\n'
    #     'stage.jewelersmutual.com/protectanglo\n'
    #     'stage.jewelersmutual.com/protectbloomingrings\n'
    #     'stage.jewelersmutual.com/protectdercodiamonds\n'
    #     'stage.jewelersmutual.com/protectfrankdarling\n'
    #     'stage.jewelersmutual.com/protectgemsby\n'
    #     'stage.jewelersmutual.com/protection\n'
    #     'stage.jewelersmutual.com/protectjewelryexpo\n'
    #     'stage.jewelersmutual.com/protectprestigetime\n'
    #     'stage.jewelersmutual.com/protectsummitdiamond\n'
    #     'stage.jewelersmutual.com/quickpay\n'
    #     'stage.jewelersmutual.com/quote\n'
    #     'stage.jewelersmutual.com/quotes\n'
    #     'stage.jewelersmutual.com/resources\n'
    #     'stage.jewelersmutual.com/subscribe\n'
    #     'stage.jewelersmutual.com/travel\n'
    #     'stage.jewelersmutual.com/travelguide\n'
    #     'stage.jewelersmutual.com/uploadappraisal\n'
    #     'stage.jewelersmutual.com/worth\n'
    #     'stage.jewelersmutual.com/_Bluenile\n'
    #     'stage.jewelersmutual.com/Home\n'
    #     'stage.jewelersmutual.com/clarity-blog/10-ways-to-protect-your-business-while-on-vacation\n'
    #     'stage.jewelersmutual.com/clarity-blog/11-reminders-in-response-to-the-new-york-diamond-district-robbery\n'
    #     'stage.jewelersmutual.com/clarity-blog/12-recent-jewelry-crimes-in-california-what-you-can-do-to-stay-safe\n'
    #     'stage.jewelersmutual.com/clarity-blog/16-ways-to-stay-alert-for-check-credit-card-fraud\n'
    #     'stage.jewelersmutual.com/clarity-blog/2-factors-for-optimal-physical-security\n'
    #     'stage.jewelersmutual.com/clarity-blog/3-essential-precautions-to-reduce-the-chance-of-a-robbery\n'
    #     'stage.jewelersmutual.com/clarity-blog/3-jewelry-store-promotion-ideas-that-dont-cost-a-dime\n'
    #     'stage.jewelersmutual.com/clarity-blog/3-tips-all-jewelers-should-know-when-preparing-for-holiday-sales\n'
    #     'stage.jewelersmutual.com/clarity-blog/3-tips-on-how-to-engage-employees-at-jewelry-businesses\n'
    #     'stage.jewelersmutual.com/clarity-blog/4-1-tips-for-protecting-electronic-equipment-from-power-surges\n'
    #     'stage.jewelersmutual.com/clarity-blog/4-lessons-6-actions-to-take-to-prevent-a-throw-away-loss\n'
    #     'stage.jewelersmutual.com/clarity-blog/4-risks-of-using-a-jewelry-memo\n'
    #     'stage.jewelersmutual.com/clarity-blog/4-steps-for-recovery-after-a-storm\n'
    #     'stage.jewelersmutual.com/clarity-blog/4-things-to-consider-before-taking-possession-of-a-customers-jewelry\n'
    #     'stage.jewelersmutual.com/clarity-blog/4-ways-to-personal-jewelry-insurance-keeps-you-in-touch-with-customers\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-minute-staff-meetings-can-help-prevent-lapses-in-procedural-security\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-safety-tips-during-the-most-vulnerable-times-for-jewelry-businesses\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-tips-for-how-to-receive-jewelry\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-tips-to-recognize-warning-signs-of-casing\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-types-of-jewelry-store-thefts-and-how-to-prevent-them\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-ways-for-jewelers-to-reduce-the-risk-of-internal-theft\n'
    #     'stage.jewelersmutual.com/clarity-blog/5-ways-to-back-up-surveillance-footage\n'
    #     'stage.jewelersmutual.com/clarity-blog/6-pieces-of-home-security-advice-for-jewelers\n'
    #     'stage.jewelersmutual.com/clarity-blog/6-takeaway-from-jsas-2015-annual-crime-report\n'
    #     'stage.jewelersmutual.com/clarity-blog/6-tips-for-hiring-a-security-guard-for-special-events\n'
    #     'stage.jewelersmutual.com/clarity-blog/7-lessons-for-keeping-high-value-jewelry-safe\n'
    #     'stage.jewelersmutual.com/clarity-blog/7practical-tips-for-preventing-smash-and-grab-robberies\n'
    #     'stage.jewelersmutual.com/clarity-blog/7-tips-for-annual-jewelry-inventory-management\n'
    #     'stage.jewelersmutual.com/clarity-blog/7-tips-for-jewelers-to-reduce-the-risk-of-data-breach\n'
    #     'stage.jewelersmutual.com/clarity-blog/7-tips-for-staying-safe-at-jewelry-trade-shows\n'
    #     'stage.jewelersmutual.com/clarity-blog/8-tips-to-keep-emails-safe-at-your-jewelry-business\n'
    #     'stage.jewelersmutual.com/clarity-blog/9-things-to-keep-in-mind-when-setting-up-a-safe\n'
    #     'stage.jewelersmutual.com/clarity-blog/advice-for-developing-emergency-evacuation-procedures\n'
    #     'stage.jewelersmutual.com/clarity-blog/a-jewelers-of-america-professional-certification-can-help-you-succeed\n'
    #     'stage.jewelersmutual.com/clarity-blog/alarms-101-basics-of-alarm-security\n'
    #     'stage.jewelersmutual.com/clarity-blog/an-umbrella-policy-could-be-the-key-to-saving-your-business\n'
    #     'stage.jewelersmutual.com/clarity-blog/a-year-of-security-advice-for-jewelers\n'
    #     'stage.jewelersmutual.com/clarity-blog/black-friday-security-for-jewelers-simple-and-effective-strategies\n'
    #     'stage.jewelersmutual.com/clarity-blog/build-loyalty-with-your-customers-and-educate-them-about-the-5th-c\n'
    #     'stage.jewelersmutual.com/clarity-blog/burglary-alarm-systems-will-yours-work-in-2017\n'
    #     'stage.jewelersmutual.com/clarity-blog/burglary-alert-4-characteristics-of-jewelry-crimes-in-california\n'
    #     'stage.jewelersmutual.com/clarity-blog/check-out-the-webinar-on-social-media-opportunities-and-risks\n'
    #     'stage.jewelersmutual.com/clarity-blog/credit-card-technology-is-changing-it-will-impact-your-business\n'
    #     'stage.jewelersmutual.com/clarity-blog/data-compromise-is-a-risk-for-every-business-learn-how-to-protect-yours\n'
    #     'stage.jewelersmutual.com/clarity-blog/dollars-sense-11-pieces-of-cash-handling-advice-for-jewelers\n'
    #     'stage.jewelersmutual.com/clarity-blog/dont-be-fooled-7-tips-for-jewelers-buying-gold\n')
    #     time.sleep(3)
    #     driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section[2]/div/form/div[2]/div/a').click()
    #     time.sleep(5)
    #     driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]').click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]/span[1]/select/optgroup/option[4]').click()
    #     time.sleep(5)
    #     if driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]').click():
    #         time.sleep(5)
    #         driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]/select/optgroup/option[3]').click()
    #         time.sleep(10)
    #         errors = driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text
    #         print(driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text)
    #         driver.back()
    #         assert errors == '0 URLs', '404 status in redirection links'
    #     else:
    #         driver.back()
    #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
    #         text_area = driver.find_element_by_class_name('textarea')
    #         text_area.click()
    #         text_area.click()
    #         time.sleep(2)
    #         text_area.send_keys('stage.jewelersmutual.com/clarity-blog/features-to-consider-for-your-jewelry-inventory-software\n'
    #         'stage.jewelersmutual.com/clarity-blog/help-educate-your-customers-about-jewelry-insurance-with-our-new-ebook\n'
    #         'stage.jewelersmutual.com/clarity-blog/holiday-season-security-gets-jewelers-ready-for-the-busy-days-ahead\n'
    #         'stage.jewelersmutual.com/clarity-blog/holiday-season-security-in-under-5-minutes\n'
    #         'stage.jewelersmutual.com/clarity-blog/holiday-season-security-video-provides-timely-advice-for-jewelers\n'
    #         'stage.jewelersmutual.com/clarity-blog/home-security-tips-for-jewelers-electronic-security\n'
    #         'stage.jewelersmutual.com/clarity-blog/home-security-tips-for-jewelers-physical-security\n'
    #         'stage.jewelersmutual.com/clarity-blog/home-security-tips-for-jewelers-procedural-security\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-do-i-know-if-im-being-cased-be-alert-for-these-5-warning-signs\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-improve-your-jewelry-store-security-for-free\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-keep-your-jewelry-business-safe-on-social-media\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-layer-your-jewelry-store-security-from-front-to-back\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-make-a-disaster-plan-for-your-jewelry-business\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-prepare-for-a-hurricane-protecting-your-building\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-prepare-for-a-hurricane-what-you-can-expect-in-2016\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-prevent-a-three-minute-burglary-the-golden-rule-5-tips\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-protect-electronic-equipment-from-power-surges\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-protect-your-jewelry-business-outside-of-normal-hours\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-recognize-fraud-red-flags-recommendations-for-combating-them\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-stay-safe-during-a-robbery-the-8-tips-jewelers-need-to-know\n'
    #         'stage.jewelersmutual.com/clarity-blog/how-to-use-a-suspicious-incident-to-improve-jewelry-store-security\n'
    #         'stage.jewelersmutual.com/clarity-blog/inventory-record-keeping-videos-for-retail-wholesale-jewelers\n'
    #         'stage.jewelersmutual.com/clarity-blog/inventory-record-keeping-your-annual-physical-inventory-in-7-steps\n'
    #         'stage.jewelersmutual.com/clarity-blog/is-a-door-buzzer-system-right-for-your-jewelry-business\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelers-block-insurance-recognizing-the-top-agents-in-the-industry\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelers-mutual-agents-do-more-than-provide-insurance\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelers-sharing-with-jewelers-denise-oros-advice-for-jewelers\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelers-sharing-with-jewelers-edmond-bakoss-success-with-relieve\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelers-sharing-with-jewelers-steve-blumbergs-story\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-2017-begins-with-widespread-crime\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-common-themes-in-robberies\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-distraction-thefts-surge-in-october\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-distraction-thefts-surge-in-october-0\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-high-profile-burglary-at-las-vegas-casino\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-robberies-make-headlines-in-may\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-crime-report-thefts-are-still-a-significant-concern\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-insurance-provides-happiness-and-peace-of-mind-for-customers\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-store-burglary-prevention-overcome-obstacles-at-closing-time\n'
    #         'stage.jewelersmutual.com/clarity-blog/jewelry-trade-shows-security-for-before-during-and-after\n'
    #         'stage.jewelersmutual.com/clarity-blog/keeping-jewelry-safe-3-holiday-safety-tips-for-your-customers\n'
    #         'stage.jewelersmutual.com/clarity-blog/last-minute-jewelry-store-security-tips-for-the-holidays\n'
    #         'stage.jewelersmutual.com/clarity-blog/loss-prevention-for-jewelry-businesses-7-questions-to-answer\n'
    #         'stage.jewelersmutual.com/clarity-blog/meet-and-greet-practices-for-customer-service-and-security\n'
    #         'stage.jewelersmutual.com/clarity-blog/millennial-insights-what-is-luxury\n'
    #         'stage.jewelersmutual.com/clarity-blog/new-service-from-jewelers-board-of-trade-aims-to-assist-non-members\n'
    #         'stage.jewelersmutual.com/clarity-blog/offset-the-liability-risks-of-winter-weather-by-doing-these-4-things\n'
    #         'stage.jewelersmutual.com/clarity-blog/optimizing-jewelry-store-security-with-physical-and-electronic-upgrades\n'
    #         'stage.jewelersmutual.com/clarity-blog/peak-hurricane-season-is-coming-dont-let-these-5-facts-fool-you\n'
    #         'stage.jewelersmutual.com/clarity-blog/pep-security-3-essential-components-for-a-safe-secure-jewelry-business\n'
    #         'stage.jewelersmutual.com/clarity-blog/prepare-and-recover-from-disasters-by-answering-these-9-questions\n'
    #         'stage.jewelersmutual.com/clarity-blog/prepare-for-hurricane-season-by-reviewing-these-materials\n'
    #         'stage.jewelersmutual.com/clarity-blog/prevent-jewelry-crime-by-sharing-your-own-advice\n'
    #         'stage.jewelersmutual.com/clarity-blog/proper-lighting-for-jewelry-businesses-can-deter-crime-day-night\n'
    #         'stage.jewelersmutual.com/clarity-blog/protect-yourself-from-the-liability-of-slip-and-fall-accidents\n'
    #         'stage.jewelersmutual.com/clarity-blog/robbery-prevention-for-jewelers-how-to-identify-casing\n'
    #         'stage.jewelersmutual.com/clarity-blog/safes-for-jewelers-what-to-consider-before-buying\n'
    #         'stage.jewelersmutual.com/clarity-blog/safety-and-security-preparations-for-jck-las-vegas-2016\n'
    #         'stage.jewelersmutual.com/clarity-blog/secure-business-series-video-puts-disaster-planning-on-your-radar\n'
    #         'stage.jewelersmutual.com/clarity-blog/secure-your-coverage-by-using-autopay-on-your-premium\n'
    #         'stage.jewelersmutual.com/clarity-blog/security-guard-services-finding-a-good-fit-for-your-jewelry-business\n'
    #         'stage.jewelersmutual.com/clarity-blog/security-guards-for-jewelry-stores-a-must-during-the-holidays\n'
    #         'stage.jewelersmutual.com/clarity-blog/security-tips-for-jck-las-vegas\n'
    #         'stage.jewelersmutual.com/clarity-blog/share-these-3-tips-with-customers-who-travel-with-jewelry\n'
    #         'stage.jewelersmutual.com/clarity-blog/slip-and-fall-lawsuits-they-can-leave-you-out-in-the-cold\n'
    #         'stage.jewelersmutual.com/clarity-blog/snow-removal-recommendations-for-businesses\n'
    #         'stage.jewelersmutual.com/clarity-blog/special-announcement-new-president-ceo-of-jewelers-mutual-announced\n'
    #         'stage.jewelersmutual.com/clarity-blog/take-caution-when-traveling-by-car\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-5-step-rooftop-burglary-procedure-criminals-use-what-you-can-do-to-stop-them\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-basic-guide-to-insurance-for-jewelers-6-terms-to-know\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-basics-of-businessowners-insurance-coverage\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-dos-and-donts-for-jewelers-treating-psychological-injuries\n'
    #         'stage.jewelersmutual.com/clarity-blog/theft-prevention-for-jewelers-warning-signs-to-be-aware-of\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-future-of-jewelry-store-security-what-to-look-for\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-multiple-benefits-of-joining-a-crime-prevention-network\n'
    #         'stage.jewelersmutual.com/clarity-blog/the-right-and-wrong-times-to-use-a-panic-button-or-duress-code\n'
    #         'stage.jewelersmutual.com/clarity-blog/tips-for-avoiding-winter-weather-liabilities\n'
    #         'stage.jewelersmutual.com/clarity-blog/tips-for-marketing-to-affluent-millennials-the-trend-seekers\n'
    #         'stage.jewelersmutual.com/clarity-blog/traveling-with-your-jewelry-inventory-tips-for-safety-on-the-road\n'
    #         'stage.jewelersmutual.com/clarity-blog/unexpected-ways-do-it-yourself-projects-cause-more-harm-than-good\n'
    #         'stage.jewelersmutual.com/clarity-blog/vaults-101-know-different-types-of-vaults-their-ratings-and-more\n'
    #         'stage.jewelersmutual.com/clarity-blog/what-can-jewelers-do-to-help-avoid-a-wrongful-termination-lawsuit\n'
    #         'stage.jewelersmutual.com/clarity-blog/what-is-dual-monitoring-tips-for-why-you-need-it-how-you-get-it\n'
    #         'stage.jewelersmutual.com/clarity-blog/what-is-employment-practices-liability-insurance\n'
    #         'stage.jewelersmutual.com/clarity-blog/when-robbery-prevention-isnt-enough-what-to-do-during-an-attack\n'
    #         'stage.jewelersmutual.com/clarity-blog/why-a-typical-smart-jewelry-warranty-can-let-your-customers-down\n'
    #         'stage.jewelersmutual.com/clarity-blog/why-google-business-photos-are-a-risk-for-your-business\n'
    #         'stage.jewelersmutual.com/clarity-blog/why-non-retail-jewelry-businesses-should-have-an-umbrella-policy\n'
    #         'stage.jewelersmutual.com/clarity-blog/why-sharing-a-suspicious-incident-logbook-can-keep-you-a-step-ahead\n'
    #         'stage.jewelersmutual.com/clarity-blog/why-ul-certified-alarms-are-essential-for-jewelers\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/10-jewelry-safety-tips-to-avoid-a-bummer-summer\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/10-parts-of-a-watch-you-should-actually-know\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/3-reasons-to-protect-a-smart-watch-you-wont-use-in-3-years\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/3-tips-for-the-perfect-engagement-ring-selfie\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/4-safe-options-for-moving-your-jewelry\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/4-ways-to-save-with-jewelers-mutual\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/5-big-names-in-jewelry-share-their-holiday-must-haves\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/5-jewelry-safety-tips-to-prepare-for-severe-weather\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/5-pieces-of-must-have-jewelry-to-build-a-capsule-jewelry-wardrobe\n'
    #         'stage.jewelersmutual.com/the-jewelry-box/5-questions-to-ask-your-jeweler-when-buying-an-engagement-ring\n')
    #         time.sleep(3)
    #         driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section[2]/div/form/div[2]/div/a').click()
    #         time.sleep(5)
    #         driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]').click()
    #         time.sleep(2)
    #         driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]/span[1]/select/optgroup/option[4]').click()
    #         time.sleep(5)
    #         if driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]').click():
    #             time.sleep(5)
    #             driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]/select/optgroup/option[3]').click()
    #             time.sleep(10)
    #             errors = driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text
    #             print(driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text)
    #             driver.back()
    #             assert errors == '0 URLs', '404 status in redirection links'
    #         else:
    #             driver.back()
    #             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
    #             text_area = driver.find_element_by_class_name('textarea')
    #             text_area.click()
    #             text_area.click()
    #             time.sleep(2)
    #             text_area.send_keys('stage.jewelersmutual.com/the-jewelry-box/5-summer-jewelry-trends-for-2015\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/5-ways-charity-jewelry-is-changing-the-world-photos\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/a-beginners-guide-to-3d-printed-jewelry\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/a-beginners-guide-to-choosing-a-jeweler\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/a-diamond-hunt-awaits-you-in-arkansas\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/an-illustrated-guide-to-engagement-ring-insurance-infographic\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/band-together-helping-others-one-vote-at-a-time\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/birthstone-for-august-a-nod-to-nature-with-peridot\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/birthstone-for-june-using-pearls-in-your-wedding\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/can-i-shower-with-my-engagement-ring-on\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/compare-diamond-shapes-by-carat-weight-diamond-size-chart\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/crazy-facts-about-nba-championship-rings-that-will-impress-your-friends\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/designer-spotlight-cartier\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/dos-and-donts-of-spring-cleaning-your-jewelry\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/dressing-downton-costumes-jewelry-on-display-in-traveling-exhibition\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/getting-a-jewelry-appraisal-is-simple\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/holiday-gift-ideas-for-jewelry-lovers\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-much-does-it-cost-to-insure-an-engagement-ring\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-much-does-it-cost-to-resize-a-ring\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-much-should-a-jewelry-appraisal-for-insurance-cost\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-clean-a-watch-safely\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-decorate-with-diamonds-designer-interview\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-file-a-jewelry-insurance-claim\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-navigate-the-airport-while-traveling-with-jewelry\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-pack-jewelry-for-travel-video\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-stack-your-jewelry-this-summer\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-store-jewelry-on-the-go\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-travel-with-jewelry-safely\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/last-minute-bridal-accessories-you-can-get-within-a-week\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/lost-ring-down-the-drain-dont-panic\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/need-proposal-help-8-marriage-proposal-ideas-that-keep-it-simple\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/recycled-jewelry-a-tale-of-two-earrings\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/red-white-and-blue-jewelry-you-can-wear-beyond-the-4th-of-july\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/running-jewelry-a-reward-for-your-race\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/septembers-birthstone-sapphires-inspired-by-the-stars\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/smart-jewelry-that-wont-ruin-your-outfit\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/the-best-choice-when-you-need-the-strongest-metal-for-a-wedding-band\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/top-3-jewelry-gifts-for-the-season\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/top-5-favorite-blog-posts-of-2015\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/top-smart-jewelry-picks-for-every-guy\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/traveling-with-jewelry-what-to-do-before-you-leave\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/traveling-with-jewelry-what-to-do-when-you-get-back\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/traveling-with-jewelry-what-to-do-while-youre-gone\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/travel-jewelry-the-industrys-best-kept-secret\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/using-a-homemade-jewelry-cleaner-avoid-these-3\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/what-its-like-to-be-pre-engaged\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/what-to-do-when-you-cant-get-your-ring-off\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/when-and-how-to-make-a-ring-smaller-without-resizing\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/when-not-to-wear-your-wedding-ring-this-summer\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/where-to-keep-the-engagement-ring-before-proposing\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/why-you-need-to-keep-a-personal-jewelry-inventory\n'
    #             'stage.jewelersmutual.com/clarity-blog/how-to-stay-safe-on-social-media-6-questions-to-ask-yourself\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/the-forgotten-step-to-planning-a-valentines-day-proposal\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/keep-your-jewelry-covered-for-current-value\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/5-ways-to-protect-your-jewelry-in-winter\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/6-tips-to-keeping-jewelry-safe-at-home\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/history-of-the-wedding-ring\n'
    #             'stage.jewelersmutual.com/jmuniversity\n'
    #             'stage.jewelersmutual.com/QuickBillPay\n'
    #             'stage.jewelersmutual.com/Partners/BlueNile\n'
    #             'stage.jewelersmutual.com/Log-In\n'
    #             'stage.jewelersmutual.com/Business\n'
    #             'stage.jewelersmutual.com/Personal\n'
    #             'stage.jewelersmutual.com/Personal-Jewelry-Insurance\n'
    #             'stage.jewelersmutual.com/newsroom\n'
    #             'stage.jewelersmutual.com/propose\n'
    #             'stage.jewelersmutual.com/protectgemandjewel\n'
    #             'stage.jewelersmutual.com/protectpointnopointstudio\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/10-proposal-tips-that-will-keep-the-ring-safe\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/7-rules-to-keep-jewelry-safe-during-a-move\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/7-tips-to-travel-with-jewelry-safely\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/fall-in-love-with-3-fall-jewelry-trends\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/getting-real-about-jewelry-insurance-3-customer-stories\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/gloves-the-most-dangerous-accessory-of-all\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-insure-a-ring-without-spoiling-the-surprise\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/is-your-child-too-young-for-jewelry\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/pearls-the-long-and-short-of-staying-on-trend\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/your-weight-loss-could-put-your-jewelry-at-risk\n'
    #             'stage.jewelersmutual.com/protectwilliambarthman\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-jewelry-insurance-works-replacement-vs-reimbursement\n'
    #             'stage.jewelersmutual.com/Legal/Privacy-Policy\n'
    #             'stage.jewelersmutual.com/contact-us\n'
    #             'stage.jewelersmutual.com/Legal/Terms-and-conditions-of-usage\n'
    #             'stage.jewelersmutual.com/personal-jewelry-insurance/what-we-offer/our-coverage\n'
    #             'stage.jewelersmutual.com/getcovered\n'
    #             'stage.jewelersmutual.com/protectbilligjewelers\n'
    #             'stage.jewelersmutual.com/protectjewelsbyiroff\n'
    #             'stage.jewelersmutual.com/protectzola\n'
    #             'stage.jewelersmutual.com/ritani\n'
    #             'stage.jewelersmutual.com/protectsickingersjewelry\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/how-to-propose-4-thoughts-popping-the-question\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/what-to-do-before-the-proposal\n'
    #             'stage.jewelersmutual.com/protectheritage\n'
    #             'stage.jewelersmutual.com/clarity-blog/cutting-the-power-new-trend-jewelry-store-burglaries\n'
    #             'stage.jewelersmutual.com/protectanyedesigns\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/3-reasons-to-protect-smart-watch-you-wont-use-3-years\n'
    #             'stage.jewelersmutual.com/testimonial\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/what-to-do-before-proposing\n'
    #             'stage.jewelersmutual.com/the-jewelry-box/picking-an-engagement-ring-4-thoughts-to-consider\n')
    #             time.sleep(3)
    #             driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section[2]/div/form/div[2]/div/a').click()
    #             time.sleep(5)
    #             driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]').click()
    #             time.sleep(2)
    #             driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]/span[1]/select/optgroup/option[4]').click()
    #             time.sleep(5)
    #             if driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]').click():
    #                 time.sleep(5)
    #                 driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]/select/optgroup/option[3]').click()
    #                 time.sleep(10)
    #                 errors = driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text
    #                 print(driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text)
    #                 driver.back()
    #                 assert errors == '0 URLs', '404 status in redirection links'
    #             else:
    #                 driver.get(Redirect_url)
    #                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
    #                 text_area = driver.find_element_by_class_name('textarea')
    #                 text_area.click()
    #                 text_area.click()
    #                 time.sleep(2)
    #                 text_area.send_keys('stage.jewelersmutual.com/the-jewelry-box/how-to-clean-care-your-engagement-ring\n'
    #                 'stage.jewelersmutual.com/the-jewelry-box/ring-appraisal-what-you-need-to-know-insurance\n'
    #                 'stage.jewelersmutual.com/protectoliveave\n')
    #                 time.sleep(3)
    #                 driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section[2]/div/form/div[2]/div/a').click()
    #                 time.sleep(5)
    #                 driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]').click()
    #                 time.sleep(2)
    #                 driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[1]/span[1]/select/optgroup/option[4]').click()
    #                 time.sleep(5)
    #                 if driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]').click():
    #                     time.sleep(5)
    #                     driver.find_element_by_xpath('//*[@id="results"]/div/div/div[2]/div/div[3]/span[1]/select/optgroup/option[3]').click()
    #                     time.sleep(10)
    #                     errors = driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text
    #                     print(driver.find_element_by_xpath('//*[@id="results"]/div/div/div[3]/div/div[2]/div[1]').text)
    #                     driver.back()
    #                     assert errors == '0 URLs', '404 status in redirection links'
    # assert 'alex' == 'alex'













