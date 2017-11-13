# Import libraries
import time
import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from twilio.rest import Client

# Settings for web
CASE_ID = 'I-200-17283-283733'
HOMEPAGE = 'https://icert.doleta.gov/index.cfm?event=ehRegister.caseStatusSearch'
KPMG = 'https://www.kpmglaw.ca/Gips_Client'
USER = 'sWANG920'
PASS = '********'
driver = webdriver.Chrome('chromedriver.exe')
driver_2 = webdriver.Chrome('chromedriver.exe')


# Settings for SMS
accountSID = 'AC913d64d8635faab14cb3ffe8608d5485'
authToken = '469d1a8c1b12c938a901f92451d8d06b'
client = Client(accountSID,authToken)
myTwilioNumber = '+19522609448'
myCellPhone = '+18572007368'
    
# Start!!
while(True):
    driver.get(HOMEPAGE)
    elem = driver.find_element_by_name('caseNumbers')
    elem.send_keys(CASE_ID)
    time.sleep(5)
    elem = driver.find_element_by_name('Searchcases')
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
    elem = driver.find_element_by_class_name('titleCase')
    result1 = elem.get_attribute('title')
    
    driver_2.get(KPMG)
    elem = driver_2.find_element_by_name('ctl00$MainContent$tb_Username')
    elem.send_keys(USER)
    elem = driver_2.find_element_by_name('ctl00$MainContent$tb_Password')
    elem.send_keys(PASS)
    elem = driver_2.find_element_by_name('ctl00$MainContent$btn_login')
    elem.send_keys(Keys.RETURN)
    time.sleep(20)
    elem = driver_2.find_element_by_id('ctl00_ctl00_MainContent_gv_ListOfAssignment_ctl02_lnk_ProcessId')
    elem.send_keys(Keys.RETURN)
    time.sleep(30)
    elem = driver_2.find_element_by_link_text('Milestone Information')
    elem.send_keys(Keys.RETURN)
    time.sleep(20)
    elem = driver_2.find_element_by_id('ctl00_ctl00_MainContent_assignmentContent_gv_Milestones_ctl02_lb_gv_startDate')
    result2 = elem.text
    elem = driver_2.find_element_by_link_text('Logout') 
    elem.send_keys(Keys.RETURN)

    now = datetime.datetime.now()
    if(now.hour <= 24 and now.hour >= 8):
        if result1 == 'in process' and result2 == '10/17/2017':
            message = client.messages.create(body='No Updates', from_=myTwilioNumber, to=myCellPhone)
            time.sleep(5400)
        else:
            message = client.messages.create(body='Updated', from_=myTwilioNumber, to=myCellPhone)
    else:
        time.sleep(5400)
