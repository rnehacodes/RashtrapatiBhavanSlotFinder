from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.scraping_utils import *
import time

#Open the website in chrome
website = 'https://visit.rashtrapatibhavan.gov.in/plan-visit/rb-main-building/nR/jR'
driver = webdriver.Chrome()
driver.get(website)

#Get the year value from the year selected by default i.e. current year
current_year = getSelectedYear(driver)

#Get the months available
months = getMonths(driver)

#Get the month from the month selected by default i.e. current month
selected_month = getSelectedMonth(driver)

#Print the dates having open slots in the current(by default selected month)
dates = findAvailableDates(driver)
for date in dates :
    print(date.text + " " + selected_month.text+ " " + current_year.text)

#Traverse through every month and fetch the available dates


#select the next month
##Click on the month dropdown
select_month = Select(driver.find_element(By.CLASS_NAME, 'ui-datepicker-month'))

# Select next month option by index
select_month.select_by_index(1)
selected_month = driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']/option[@selected='selected']")

print(selected_month.text)

driver.quit()