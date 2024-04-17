from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def getSelectedMonth(driver):
    return driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']/option[@selected='selected']")

def getSelectedYear(driver):
    return driver.find_element(By.XPATH, "//select[@data-handler='selectYear']/option[@selected='selected']")

def findAvailableDates(driver):
    return driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']")

def getMonths(driver):
    return driver.find_elements(By.XPATH, "//select[@data-handler='selectMonth']/option")
