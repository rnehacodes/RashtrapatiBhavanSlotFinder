from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Open the website in chrome
driver = webdriver.Chrome()

def openWebsite(website):
    driver.get(website)

def getSelectedMonth():
    return driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']/option[@selected='selected']")

def getSelectedYear():
    return driver.find_elements(By.XPATH, "//select[@data-handler='selectYear']/option[@selected='selected']")

def findAvailableDates():
    # driver.find_element(By.CLASS_NAME, "calendar hasDatepicker")
    return driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']")

def findAvailableSlots():
    return driver.find_elements(By.XPATH, '//li[@class="time-bg slot"]')

def getSlotTime():
    return driver.find_element(By.XPATH, "//*[@class='time-bg slot']")

def getSlotSeats():
    return driver.find_element(By.TAG_NAME, 'span')

def getMonths():
    return driver.find_elements(By.XPATH, "//select[@data-handler='selectMonth']/option")

def getYears():
    return driver.find_elements(By.XPATH, "//select[@data-handler='selectYear']/option")

def selectNextYear(y):
    #Click on the year dropdown
    select_year = Select(driver.find_element(By.CLASS_NAME, 'ui-datepicker-year'))
    #select the next year by index
    select_year.select_by_index(y)

def selectNextMonth(m):
    #Click on the month dropdown
    select_month = Select(driver.find_element(By.CLASS_NAME, 'ui-datepicker-month'))
    #select the next month by index
    select_month.select_by_index(m)

def selectDate(dateValue):
    #Click on the month dropdown
    date = driver.find_element(By.XPATH, f"//a[@data-date='{dateValue}']")
    # date.click()
    driver.execute_script("arguments[0].click();", date)
