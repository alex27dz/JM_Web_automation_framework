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
from JM_Elem_Config import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def navbar_validation(driver):
    print('verifying Navbar')
    try:
        url = '/jewelry-engagement-ring-insurance-quote'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]')))

        print('Personal')
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        time.sleep(1)
        print('Personal passed')

        print('Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Appraisal Solution').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        time.sleep(1)
        print('Business passed')

        print('Answers')
        url = '/jewelry-insurance-101'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        time.sleep(1)
        print('Answers passed')

        print('About Us')
        url = '/about-us'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        time.sleep(1)
        print('About Us passed')

        print('Log In')
        driver.find_element_by_xpath('//a[contains(@href,"https://my.jewelersmutual.com/PLPortal/Security/")]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Personal Jewelry').text)
        print(driver.find_element_by_link_text('Agent').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        time.sleep(1)
        print('Log In passed')
        print('Navbar - verifyied')
        return True
    except:
        return False

def footer_validation(driver):
    print('verifying Footer')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'block-footerplmenu')))
        print('Personal')
        print(driver.find_element_by_id('block-footerplmenu').text)
        print('Personal passed')

        print('Business')
        print(driver.find_element_by_id('block-footerclmenu').text)
        print('Business passed')

        print('About')
        print(driver.find_element_by_id('block-footerinfomenu').text)
        print('About passed')

        print('Contact')
        print(driver.find_element_by_id('block-footercontactmenu').text)
        print('Contact passed')

        print('BLOG')
        print(driver.find_element_by_id('block-footerrecommendedcontentlinks').text)
        print('BLOG passed')
        print('Footer - verifyied')
        return True
    except:
        return False

#def Personal_insurance_Body_validation(driver):
# driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
# driver.get("https://stage.jewelersmutual.com/jewelry-engagement-ring-insurance-quote")
# time.sleep(3)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'What will it cost me?')]")))
# print(driver.find_element_by_xpath("//a[contains(text(),'What will it cost me?')]").text)
#
# time.sleep(1)
# print('Body passed')
#



