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


# print(driver.find_element_by_xpath("//div[contains(@class, '')]").text)
# print(driver.find_element_by_id('').text)
# print(driver.find_element_by_class_name('').text)


def navbar_validation(driver):
    print('verifying Navbar containers')
    try:
        url = '/jewelry-engagement-ring-insurance-quote'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]')))
        time.sleep(2)
        print('Navbar Personal')
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        time.sleep(1)
        print('Navbar Personal passed')
        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        # print(driver.find_element_by_link_text('Appraisal Solution').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        time.sleep(1)
        print('Navbar Business passed')
        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        time.sleep(1)
        print('Navbar Answers passed')
        print('Navbar About Us')
        url = '/about-us'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        time.sleep(1)
        print('Navbar About Us passed')
        print('Navbar Log In')
        driver.find_element_by_xpath('//a[contains(@href,"https://my.jewelersmutual.com/PLPortal/Security/")]').click()
        time.sleep(1)
        print(driver.find_element_by_link_text('Personal Jewelry').text)
        print(driver.find_element_by_link_text('Agent').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        time.sleep(1)
        print('Navbar Log In passed')
        print('Navbar - verifyied')
        return True
    except:
        return False


def footer_validation(driver):
    print('verifying Footer containers')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'block-footerplmenu')))
        print('Footer Personal')
        element = driver.find_element_by_id('block-footerplmenu')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('block-footerplmenu').text)
        print('Footer Personal passed')
        print('Footer Business')
        print(driver.find_element_by_id('block-footerclmenu').text)
        print('Footer Business passed')
        print('Footer About')
        print(driver.find_element_by_id('block-footerinfomenu').text)
        print('Footer About passed')
        print('Footer Contact')
        print(driver.find_element_by_id('block-footercontactmenu').text)
        print('Contact passed')
        print('Footer BLOG')
        print(driver.find_element_by_id('block-footerrecommendedcontentlinks').text)
        print('Footer BLOG passed')
        time.sleep(2)
        print('Footer - verifyied')
        return True
    except:
        return False


def personal_insurance_body_validation(driver):
    print('verifying Personal_insurance_Body containers')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'What will it cost me?')]")))
        print(driver.find_element_by_xpath("//a[contains(text(),'What will it cost me?')]").text)
        element = driver.find_element_by_id('title-4366')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('title-4366').text)
        print(driver.find_element_by_class_name('comparison-table__center').text)
        print(driver.find_element_by_class_name('table-footer').text)
        print(driver.find_element_by_id('title-4331').text)
        print(driver.find_element_by_id('info-grid-4356').text)
        print(driver.find_element_by_id('text-image-row-4326').text)
        print(driver.find_element_by_id('image-container-8266').text)
        print(driver.find_element_by_id('title-4361').text)
        print(driver.find_element_by_id('image-container-8271').text)
        print(driver.find_element_by_id('feature-row-6476').text)
        element = driver.find_element_by_id('feature-row-4396')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('feature-row-4396').text)
        time.sleep(1)
        print('Personal_insurance_Body - verifyied')
        return True
    except:
        return False


def get_a_quote_body_validation(driver):
    print('verifying Get_A_Quote_Body containers')
    try:
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "appHeaderContainer")))
        print(driver.find_element_by_id('HeaderImages').text)
        print(driver.find_element_by_id('QuestionsContainer').text)
        element = driver.find_element_by_id('quoteContainer')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('quoteContainer').text)
        print(driver.find_element_by_id('quoteInfoNext').text)
        print(driver.find_element_by_id('right-panel').text)
        element = driver.find_element_by_id('left-panel')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('left-panel').text)
        print(driver.find_element_by_id('appHeaderContainer').text)
        print(driver.find_element_by_id('TermsAndPrivacyFooterContainer').text)
        element = driver.find_element_by_id('TermsAndPrivacyFooterContainer')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(3)
        print('Get_A_Quote_Body - verifyied')
        return True
    except:
        return False


def pay_my_bill_body_validation(driver):
    print('verifying Get_A_Quote_Body containers')
    try:
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jm-logo")))
        print(driver.find_element_by_class_name('jm-logo').text)
        element = driver.find_element_by_id('lookupForm')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('lookupForm').text)
        print(driver.find_element_by_id('continueButton').text)
        print(driver.find_element_by_id('recaptcha').text)
        print(driver.find_element_by_class_name('navbar').text)
        element = driver.find_element_by_xpath("//div[contains(@class, 'col-md-8 col-sm-6 col-xs-12')]")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_xpath("//div[contains(@class, 'container')]").text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'row')]").text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'col-md-8 col-sm-6 col-xs-12')]").text)
        time.sleep(3)
        print('Pay_My_Bill_Body - verifyied')
        return True
    except:
        return False


def claims_body_validation(driver):
    print('verifying claims_Body containers')
    try:
        time.sleep(3)
        print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container hero__image-container--no-mobile-image')]").text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--content')]").text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'content-lg text-center')]").text)
        print(driver.find_element_by_id('title-2801').text)
        print(driver.find_element_by_id('info-grid-2826').text)
        print(driver.find_element_by_id('feature-row-6726').text)
        print(driver.find_element_by_id('title-8256').text)
        print(driver.find_element_by_id('text-image-row-2841').text)
        print(driver.find_element_by_id('text-image-row-2856').text)
        print(driver.find_element_by_id('text-image-row-2851').text)
        print(driver.find_element_by_id('image-container-8276').text)
        element = driver.find_element_by_id('feature-row-2861')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('feature-row-2861').text)
        print(driver.find_element_by_id('image-container-8281').text)
        print(driver.find_element_by_id('feature-row-8261').text)
        print(driver.find_element_by_id('info-grid-2921').text)
        print(driver.find_element_by_id('title-4196').text)
        print(driver.find_element_by_id('accordion').text)
        print(driver.find_element_by_id('feature-row-8916').text)
        element = driver.find_element_by_id('text-image-row-2846')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        print(driver.find_element_by_id('text-image-row-2846').text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blocktext-image-row')]").text)
        print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blocktext-image-row')]").text)
        time.sleep(3)
        print('claims_Body - verifyied')
        return True
    except:
        return False


# driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
# driver.get('https://stage.jewelersmutual.com/jewelry-insurance-claims')
# claims_body_validation(driver)


