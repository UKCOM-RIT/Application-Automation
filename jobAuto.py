from selenium import webdriver
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##from selenium.common.exceptions import TimeoutException
import time
import math
import os
import platform
from math import ceil

class Webscraper:
    
    def __init__(self, siteAddress, username, password, desktopDir, userOS, userDistro):
        self._siteAddress = siteAddress
        self._username = username
        self._password = password
        self._desktopDir = desktopDir
        self._userOS = userOS
        self._userDistro = userDistro
        
    @property
    def siteAddress(self):
        #for questions about @property (https://python.swaroopch.com/oop.html)
        return self._siteAddress
    @siteAddress.setter
    def setSiteAddress(self, site):
        self._siteAddress = site       
    @property
    def username(self):
        return self._username
    @username.setter
    def setusername(self, usr):
        self._username = usr
    @property
    def password(self):
        return self._password
    @password.setter
    def setpassword(self, passwrd):
        self._password = passwrd       
    @property
    def desktopDir(self):
        return self._desktopDir
    @property
    def userOS(self):
        return self._userOS
    @property
    def userDistro(self):
        return self._userDistro

    def createNameArray(self, nameArray):
        #Rename all elements of name list to be last_first
        for name in range (len(nameArray)):
            nameArray[name] = nameArray[name].replace(", ", "_")
            print(nameArray[name])
        return nameArray

    def createFolder(self, directory):
        #credit: keithwaver github
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                #mkdir = single cell dir, makedirs = mutiple level 
        except OSERROR:
                print ('Error: Creating directory. ' + directory)
        return
    
    def loadPage(self):
        
        driver.get(self.siteAddress)
        username = driver.find_element_by_id("user_username")
        password = driver.find_element_by_id("user_password")
        username.send_keys(self.username)
        password.send_keys(self.password)
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
        vitaList = []
        letterList = []
        requestList = []
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
                if link == 0:
                    link = 1
                print(tempList[link].get_attribute('innerHTML'))
                linksList.append(tempList[link].get_attribute('innerHTML'))
                vitaList.append(driver.find_elements_by_partial_link_text("Vita"))
                letterList.append(driver.find_elements_by_partial_link_text("Letter"))
                requestList.append(driver.find_elements_by_partial_link_text("Request"))
        print("end of loadPage()")
        nameArray = self.createNameArray(linksList)
        for i in range(len(nameArray)):
            tempPath = self.desktopDir + nameArray[i]
            self.createFolder(tempPath)
        #Debugging Tools
        previousLink = driver.find_element_by_class_name('previous_page')
        driver.execute_script("window.scrollTo(0, 2560)")
        
        return
            
    ##    print(linksList[0].get_attribute('innerHTML'))
    
driver = webdriver.Safari()
ospath  = os.path.expanduser('~')
directory =  ospath + '/Desktop/pythonTest/'

Page  = Webscraper('https://ukjobs.uky.edu/hr/login', 'gu922972', 'lecturer19', directory, None, None)
Page.loadPage()

##driver.quit()
#Closes ALL open browser tabs

#createNameArray(linksList)
    

