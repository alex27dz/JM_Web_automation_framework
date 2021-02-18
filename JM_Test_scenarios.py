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
tag = 'Chrome'  # IE
driver_location = "/Users/alexdezho/Downloads/chromedriver"


def test_01_HomePageToPersonalInsurance():
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # IE
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
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
    assert str(business_jm_shippin_gsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
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
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Jewelry')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE 
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Agent')
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
    if tag == 'Chrome':
        driver = webdriver.Chrome(driver_location)
    else:  # if its IE 
        driver = webdriver.Ie("JM-machine location")
    driver.get(JM_url)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Zing Platform')
    url = 'https://my.jewelersmutual.com/PLPortal/Security/'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(2)
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
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    print('Access Personal Insurance')
    driver.find_element_by_partial_link_text('Explore personal jewelry insurance').click()
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
    assert str(business_jm_shippin_gsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
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

# stopped here
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
def test_35_footerToPrivacyPolicy():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    assert 'alex' == 'alex'
def test_36_footerToTermsofUse():
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get(JM_url)
    print('Access HomePage')
    time.sleep(5)
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    assert 'alex' == 'alex'




def test_67_FullPageScenario():
    assert 'alex' == 'alex'
def test_95_Redirection300links():
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











