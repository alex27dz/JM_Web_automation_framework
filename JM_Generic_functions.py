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
    driver.execute_script("window.scrollTo(0,0)")
    print('verifying Navbar containers')
    url = '/jewelry-engagement-ring-insurance-quote'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]')))
    print('Navbar Personal')

    if driver.current_url == 'https://stage.jewelersmutual.com/':
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        print('Navbar Personal passed')
        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        print('Navbar Business passed')
        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        print('Navbar Answers passed')
        print('Navbar About Us')
        url = '/about-us'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        print('Navbar About Us passed')
        print('Navbar Log In')
        driver.find_element_by_xpath('//a[contains(@href,"https://my.jewelersmutual.com/PLPortal/Security/")]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Jewelry').text)
        print(driver.find_element_by_link_text('Agent').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print('Navbar Log In passed')
    else:
        print('Navbar Personal')
        url = '/jewelry-engagement-ring-insurance-quote'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        print('Navbar Personal passed')

        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]') # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        print('Navbar Business passed')

        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        print('Navbar Answers passed')

        print('Navbar About Us')
        url = '/about-us'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        print('Navbar About Us passed')

        print('Navbar Log In')
        url = 'https://my.jewelersmutual.com/PLPortal/Security/'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Jewelry').text)
        print(driver.find_element_by_link_text('Agent').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print('Navbar Log In passed')

    print('Navbar - verifyied')
    return True


def footer_validation(driver):
    driver.execute_script("window.scrollTo(0,4000)")
    time.sleep(2)
    print('verifying Footer containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'block-footerplmenu')))
    print('Footer Personal')
    element = driver.find_element_by_id('block-footerplmenu')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
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
    print('Footer - verifyied')
    return True


def personal_insurance_body_validation(driver):
    print('verifying Personal_insurance_Body containers')
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


def get_a_quote_body_validation(driver):
    print('verifying Get_A_Quote_Body containers')
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


def pay_my_bill_body_validation(driver):
    print('verifying Get_A_Quote_Body containers')
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


def claims_body_validation(driver):
    print('verifying claims_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2801")))
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


def manage_my_policy_body_validation(driver):
    print('verifying manage_my_policy containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-apps')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'field-container')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'login-right-col')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'login-span-col')]").text)
    print(driver.find_element_by_id('jm-logo').text)
    print(driver.find_element_by_id('page-body').text)
    print(driver.find_element_by_id('body').text)
    print(driver.find_element_by_id('login-container').text)
    print(driver.find_element_by_id('AppForm').text)
    print(driver.find_element_by_id('quickPayLinkLarge').text)
    print(driver.find_element_by_id('footer-utility-links').text)
    time.sleep(3)
    print('manage_my_policy - verifyied')
    return True


def blog_body_validation(driver):
    print('verifying blog containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-personal-popular-posts')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-jewelry-box-topics')]").text)
    print(driver.find_element_by_id('block-jewelers-mutual-content').text)
    time.sleep(3)
    print('blog - verifyied')
    return True


def business_insurance_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4416")))
    print(driver.find_element_by_id('title-4416').text)
    print(driver.find_element_by_id('info-grid-4436').text)
    print(driver.find_element_by_id('title-4441').text)
    print(driver.find_element_by_id('info-grid-4481').text)
    print(driver.find_element_by_id('image-container-8286').text)
    print(driver.find_element_by_id('image-container-8311').text)
    print(driver.find_element_by_id('info-grid-8306').text)
    print(driver.find_element_by_id('text-block-4406').text)
    print(driver.find_element_by_id('video-modal-4411').text)
    print(driver.find_element_by_id('feature-row-4486').text)
    print(driver.find_element_by_id('title-8321').text)
    print(driver.find_element_by_id('related-content-9086').text)
    print(driver.find_element_by_id('title-8316').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container hero--move-image-up')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blocksalesforce-form')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodecore-pagefield-hero')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container hero__image-container--no-mobile-image')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    element = driver.find_element_by_id('title-8316')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('claims_Body - verifyied')
    return True


def business_claims_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-4596")))
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_id('text-image-row-4596').text)
    print(driver.find_element_by_id('text-image-row-4601').text)
    print(driver.find_element_by_id('text-image-row-4606').text)
    print(driver.find_element_by_id('text-image-row-4611').text)
    print(driver.find_element_by_id('feature-row-4616').text)
    print(driver.find_element_by_id('title-4646').text)
    print(driver.find_element_by_id('info-grid-4641').text)
    print(driver.find_element_by_id('accordion-4661').text)
    print(driver.find_element_by_id('feature-row-4666').text)
    element = driver.find_element_by_id('feature-row-4666')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('claims_Body - verifyied')
    return True


def business_paymybill_body_validation(driver):
    print('verifying paymybill containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lookupForm')))
    print(driver.find_element_by_id('lookupForm').text)
    print(driver.find_element_by_id('mdlHelpSampleInvoice').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navbar-collapse collapse')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'pull-lg-right pull-xl-right')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'row right-side')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'panel jm-panel-slim')]").text)
    time.sleep(3)
    print('paymybill - verifyied')
    return True


def business_zingplatform_body_validation(driver):
    print('verifying zingplatform containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-8466")))
    print(driver.find_element_by_id('title-8466').text)
    print(driver.find_element_by_id('title-8471').text)
    print(driver.find_element_by_id('video-modal-8476').text)
    print(driver.find_element_by_id('title-8366').text)
    print(driver.find_element_by_id('info-grid-7956').text)
    print(driver.find_element_by_id('image-container-8541').text)
    print(driver.find_element_by_id('title-8371').text)
    print(driver.find_element_by_id('info-grid-7981').text)
    print(driver.find_element_by_id('related-content-9036').text)
    print(driver.find_element_by_id('feature-row-8461').text)
    print(driver.find_element_by_id('accordion-9066').text)
    print(driver.find_element_by_id('feature-row-7986').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    element = driver.find_element_by_id('feature-row-7986')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('zingplatform - verifyied')
    return True


def business_jm_shippin_gsolution_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-9266")))
    print(driver.find_element_by_id('text-image-row-9266').text)
    print(driver.find_element_by_id('video-modal-9271').text)
    print(driver.find_element_by_id('info-grid-6906').text)
    print(driver.find_element_by_id('info-grid-2291').text)
    print(driver.find_element_by_id('feature-row-9276').text)
    print(driver.find_element_by_id('title-2341').text)
    print(driver.find_element_by_id('title-4191').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__eyebrow-text')]").text)
    element = driver.find_element_by_id('title-4191')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('jm_shippin_gsolution_Body - verifyied')
    return True


def business_jmcareplan_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-6046")))
    print(driver.find_element_by_id('text-block-6046').text)
    print(driver.find_element_by_id('title-6701').text)
    print(driver.find_element_by_id('title-5396').text)
    print(driver.find_element_by_id('video-modal-6706').text)
    print(driver.find_element_by_id('info-grid-5416').text)
    print(driver.find_element_by_id('info-grid-5431').text)
    print(driver.find_element_by_id('details-block-5876').text)
    print(driver.find_element_by_id('info-grid-5446').text)
    element = driver.find_element_by_id('info-grid-5446')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('jmcareplan_Body - verifyied')
    return True


def business_appraisalsolution_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-11061")))
    print(driver.find_element_by_id('title-11061').text)
    print(driver.find_element_by_id('text-block-11056').text)
    print(driver.find_element_by_id('info-grid-11081').text)
    print(driver.find_element_by_id('image-container-11066').text)
    print(driver.find_element_by_id('info-grid-11101').text)
    print(driver.find_element_by_id('video-modal-11111').text)
    print(driver.find_element_by_id('title-11116').text)
    print(driver.find_element_by_id('title-11126').text)
    print(driver.find_element_by_id('title-11131').text)
    print(driver.find_element_by_id('feature-row-11121').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black  ')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    element = driver.find_element_by_id('feature-row-11121')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('appraisalsolution_Body - verifyied')
    return True


def business_jewelerprograms_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2751")))
    print(driver.find_element_by_id('title-2751').text)
    print(driver.find_element_by_id('info-grid-2776').text)
    print(driver.find_element_by_id('image-container-9251').text)
    print(driver.find_element_by_id('feature-row-2786').text)
    print(driver.find_element_by_id('feature-row-2791').text)
    print(driver.find_element_by_id('title-9256').text)
    print(driver.find_element_by_id('title-4246').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    element = driver.find_element_by_id('title-4246')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('jewelerprograms_Body - verifyied')
    return True


def business_pawnbrokers_body_validation(driver):
    print('verifying Pawnbrokers_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4546")))
    print(driver.find_element_by_id('title-4546').text)
    print(driver.find_element_by_id('details-block-4571').text)
    print(driver.find_element_by_id('feature-row-4551').text)
    print(driver.find_element_by_id('basic-code-block-hubspot-form-for-pawnbrokers-page').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodecore-pagefield-hero')]").text)
    element = driver.find_element_by_id('basic-code-block-hubspot-form-for-pawnbrokers-page')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('Pawnbrokers_Body - verifyied')
    return True


def answers_JewelryInsurance101_body_validation(driver):
    print('verifying JewelryInsurance101_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-7541")))
    print(driver.find_element_by_id('text-image-row-7541').text)
    print(driver.find_element_by_id('related-content-7696').text)
    print(driver.find_element_by_id('related-content-8221').text)
    print(driver.find_element_by_id('title-7581').text)
    print(driver.find_element_by_id('feature-row-8511').text)
    print(driver.find_element_by_id('text-block-7601').text)
    print(driver.find_element_by_id('quote-widget-6401').text)
    print(driver.find_element_by_id('cta-group-7576').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    element = driver.find_element_by_id('cta-group-7576')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('JewelryInsurance101_Body - verifyied')
    return True


def answers_FAQ_body_validation(driver):
    print('verifying FAQ_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "views-exposed-form-acquia-search-faq-search")))
    print(driver.find_element_by_id('views-exposed-form-acquia-search-faq-search').text)
    print(driver.find_element_by_id('text-block-11376').text)
    print(driver.find_element_by_id('cta-group-9216').text)
    print(driver.find_element_by_id('text-block-11391').text)
    print(driver.find_element_by_id('cta-group-9226').text)
    print(driver.find_element_by_id('text-block-11381').text)
    print(driver.find_element_by_id('cta-group-9221').text)
    print(driver.find_element_by_id('text-block-11396').text)
    print(driver.find_element_by_id('cta-group-9231').text)
    print(driver.find_element_by_id('text-block-11386').text)
    print(driver.find_element_by_id('cta-group-9236').text)
    # print(driver.find_element_by_id('related-content-9086').text)
    print(driver.find_element_by_id('info-grid-9246').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'page-title__h1')]").text)
    element = driver.find_element_by_id('cta-group-9236')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('FAQ_Body - verifyied')
    return True


def aboutus_aboutus_body_validation(driver):
    print('verifying aboutus_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2461")))
    print(driver.find_element_by_id('title-2461').text)
    print(driver.find_element_by_id('info-grid-2506').text)
    print(driver.find_element_by_id('feature-row-2511').text)
    print(driver.find_element_by_id('title-2516').text)
    print(driver.find_element_by_id('title-2521').text)
    print(driver.find_element_by_id('text-block-2526').text)
    print(driver.find_element_by_id('info-grid-2566').text)
    print(driver.find_element_by_id('text-block-2576').text)
    print(driver.find_element_by_id('info-grid-2626').text)
    print(driver.find_element_by_id('title-2571').text)
    print(driver.find_element_by_id('text-block-2636').text)
    print(driver.find_element_by_id('info-grid-2696').text)
    print(driver.find_element_by_id('text-image-row-2706').text)
    print(driver.find_element_by_id('text-image-row-2711').text)
    print(driver.find_element_by_id('text-image-row-2716').text)
    print(driver.find_element_by_id('basic-code-block-trustpilot-about-us-horizontal').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__tout hero__tout--blue')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'layout layout--twocol-section layout--twocol-section--50-50')]").text)
    element = driver.find_element_by_id('text-image-row-2716')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('aboutus_Body - verifyied')
    return True


def aboutus_socialresponsibility_body_validation(driver):
    print('verifying socialresponsibility_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-5316")))
    print(driver.find_element_by_id('title-5316').text)
    print(driver.find_element_by_id('info-grid-5311').text)
    print(driver.find_element_by_id('text-image-row-2361').text)
    print(driver.find_element_by_id('text-image-row-2396').text)
    print(driver.find_element_by_id('text-image-row-2401').text)
    print(driver.find_element_by_id('text-image-row-2406').text)
    print(driver.find_element_by_id('title-2366').text)
    print(driver.find_element_by_id('info-grid-2391').text)
    print(driver.find_element_by_id('basic-code-block-divider-line').text)
    print(driver.find_element_by_id('feature-row-2411').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-lg-12 jm-img image1')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-md-6 jm-col-lg-6 jm-img image3')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-md-6 jm-col-lg-6 jm-img image4')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-md-6 jm-col-lg-6 jm-img image6')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-md-6 jm-col-lg-6 jm-img image5')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-md-6 jm-col-lg-12 jm-img image2')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'jm-col-xs-12 jm-col-sm-12 jm-col-md-6 jm-col-lg-12 jm-img image7')]").text)
    element = driver.find_element_by_id('feature-row-2411')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('socialresponsibility_Body - verifyied')
    return True


def aboutus_careers_body_validation(driver):
    print('verifying careers_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "feature-row-1716")))
    print(driver.find_element_by_id('feature-row-1716').text)
    print(driver.find_element_by_id('info-grid-1736').text)
    print(driver.find_element_by_id('carousel-1776').text)
    print(driver.find_element_by_id('feature-row-1781').text)
    print(driver.find_element_by_id('tab-section-4286').text)
    print(driver.find_element_by_id('feature-row-8151').text)
    print(driver.find_element_by_id('info-grid-8146').text)
    print(driver.find_element_by_id('carousel-1946').text)
    print(driver.find_element_by_id('feature-row-1816').text)
    print(driver.find_element_by_id('tab-section-4311').text)
    print(driver.find_element_by_id('feature-row-4801').text)
    print(driver.find_element_by_id('feature-row-4796').text)
    print(driver.find_element_by_id('contact-ribbon-1876').text)
    print(driver.find_element_by_id('webform-submission-careers-contact-form-block-content-771-form-ajax').text)
    print(driver.find_element_by_id('basic-code-block-google-map').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    element = driver.find_element_by_id('basic-code-block-google-map')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('careers_Body - verifyied')
    return True


def aboutus_newsroom_body_validation(driver):
    print('verifying newsroom_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-newsheroblock")))
    print(driver.find_element_by_id('block-newsheroblock').text)
    print(driver.find_element_by_id('block-jewelers-mutual-content').text)
    print(driver.find_element_by_id('text-block-8921').text)
    print(driver.find_element_by_id('text-block-8931').text)
    print(driver.find_element_by_id('text-block-8926').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'js-view-dom-id-c5e81c709443158963530345a162f16a5ef9c71e634add7585dedbc44cf8c5b3')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'js-view-dom-id-ca4d61ec14828bb8ded1a0bb3e31bb30b04bb7ec7ea8c4bf015b7f1a24db2efb')]").text)
    element = driver.find_element_by_id('text-block-8926')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('newsroom_Body - verifyied')
    return True


def login_Personal_Jewelry_body_validation(driver):
    print('verifying Personal_Jewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('jm-logo').text)
    print(driver.find_element_by_id('utility').text)
    print(driver.find_element_by_id('utility-nav-contain').text)
    print(driver.find_element_by_id('page-body').text)
    print(driver.find_element_by_id('body').text)
    print(driver.find_element_by_id('AppForm').text)
    print(driver.find_element_by_id('login-container').text)
    print(driver.find_element_by_id('footer-utility-links').text)
    time.sleep(3)
    print('Personal_Jewelry_Body - verifyied')
    return True


def login_agent_body_validation(driver):
    print('verifying agent_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "utility")))
    print(driver.find_element_by_id('utility').text)
    print(driver.find_element_by_id('utility-nav-contain').text)
    print(driver.find_element_by_id('site-nav').text)
    print(driver.find_element_by_id('page-body').text)
    print(driver.find_element_by_id('body').text)
    print(driver.find_element_by_id('AppForm').text)
    print(driver.find_element_by_id('ForgotPassword').text)
    print(driver.find_element_by_id('footer-utility-links').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'ForgotPassword')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'fn org')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'adr')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'social-icons')]").text)
    element = driver.find_element_by_id('footer-utility-links')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('agent_Body - verifyied')
    return True


def login_ZingPlatform_body_validation(driver):
    print('verifying Zing Platform_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "register-btn")))
    print(driver.find_element_by_id('register-btn').text)
    print(driver.find_element_by_id('sign-in').text)
    print(driver.find_element_by_id('prog-ind001').text)
    print(driver.find_element_by_id('bgVideo').text)
    print(driver.find_element_by_id('animate001').text)
    print(driver.find_element_by_id('prog-ind002').text)
    print(driver.find_element_by_id('prog-ind003').text)
    print(driver.find_element_by_id('prog-ind004').text)
    print(driver.find_element_by_id('prog-ind005').text)
    print(driver.find_element_by_id('prog-ind006').text)
    print(driver.find_element_by_id('myiFrameForSilentRenew').text)
    element = driver.find_element_by_id('prog-ind006')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('Zing Platform_Body - verifyied')
    return True


def body_ToRegisterForAnOnlineAccount(driver):
    print('verifying RegisterForAnOnlineAccount_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('jm-logo').text)
    print(driver.find_element_by_id('utility').text)
    print(driver.find_element_by_id('utility-nav-contain').text)
    print(driver.find_element_by_id('header-utility-links').text)
    print(driver.find_element_by_id('register-step-1').text)
    time.sleep(3)
    print('RegisterForAnOnlineAccount_Body - verifyied')
    return True


def body_startaclaim(driver):
    print('verifying careers_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lookupForm")))
    print(driver.find_element_by_id('lookupForm').text)
    print(driver.find_element_by_id('helpLookupPolicyNumber').text)
    print(driver.find_element_by_id('EmailOrPolicy').text)
    print(driver.find_element_by_id('PolicyLastName').text)
    print(driver.find_element_by_id('PolicyZipCode').text)
    print(driver.find_element_by_id('recaptcha').text)
    print(driver.find_element_by_id('continueButton').text)
    # print(driver.find_element_by_id('Thalyta example').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'navbar-brand')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'nav navbar-nav navbar-right jm-nav')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'container')]").text)
    time.sleep(3)
    print('careers_Body - verifyied')
    return True




