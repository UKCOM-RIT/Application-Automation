from selenium import webdriver
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##from selenium.common.exceptions import TimeoutException
import time
import math
from math import ceil

path = "Desktop/pythonTest/"

driver = webdriver.Safari()

def loadPage():
    driver.get('https://ukjobs.uky.edu/hr/login')
    username = driver.find_element_by_id("user_username")
    password = driver.find_element_by_id("user_password")
    username.send_keys("")
    password.send_keys("")
    driver.find_element_by_name("commit").click()

    time.sleep(10);

    applicantsLink = driver.find_element_by_link_text("Applicants")
    applicantsLink.click()
    
    time.sleep(10);

    numApplicants = driver.find_elements_by_class_name("bubble")
    numApplicants = numApplicants[0].get_attribute('innerHTML')
    #javascript scraping doesnt work, instead find the first bubble on the page

    numPages = (ceil(float(numApplicants)/30))
    #30 applicants can fit on a page

    linksList = []
    #Def & inst for next for loop
    
    for i in range (numPages):
        #all names have first & last separated by comma, tempList is Webdriver object
        if i > 0:
            nxtPageLink = driver.find_element_by_class_name('next_page')
            nxtPageLink.click()
            time.sleep(10)
        tempList = driver.find_elements_by_partial_link_text(",")
        for link in range(int(len(tempList)) -1):
            #remove last entry "If your download does not start automatically, click here."
            print(tempList[link].get_attribute('innerHTML'))
            linksList.append(tempList[link].get_attribute('innerHTML'))
    print("end of loadPage()")
    nameArray = createNameArray(linksList)
    for name in nameList:
        createFolder(path + nameArray[name])
    return
        
##    print(linksList[0].get_attribute('innerHTML'))

def createNameArray(nameArray):
    #Rename all elements of name list to be last_first
    print("Inside Name array")
    for name in range (len(nameArray)):
        nameArray[name] = nameArray[name].replace(", ", "_")
        print(nameArray[name])
    return nameArray

def createFolder(directory):
    #credit: keithwaver github
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSERROR:
            print ('Error: Creating directory. ' + directory)
    return

loadPage()
#createNameArray(linksList)
    

