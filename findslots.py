from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.scraping_utils import *
import time

#Open the website in chrome
website = 'https://visit.rashtrapatibhavan.gov.in/plan-visit/rb-main-building/nR/jR'
openWebsite(website)

year_count = 0
#Get the year values from the year dropdown
years = getYears()

#For every year, select the different months and find the subsequent dates on which the slot is available
for current_year in years :
    #For the first year, pick the year selected by default. Afterwards, select the other years available in the dropdown.
    if year_count > 0:
        selectNextYear(year_count)
    year = current_year.text
    year_count+=1

    #Get the months available
    month_count = 0
    months = getMonths()

    #For every month, select the different dates on which the slot is available
    for current_month in months:
        #For the first month, pick the month selected by default. Afterwards, select the other months available in the dropdown.
        # if month_count > 0:
        #     selectNextMonth(month_count)
        #     current_month = getSelectedMonth()
        selectNextMonth(month_count)
        current_month = getSelectedMonth()
        #Get the month from the month selected by default i.e. current month
        month = current_month.text
        month_count+=1

        #Print the dates having open slots in the current(by default selected month)
        date_count = 0
        dates = findAvailableDates()
        for i in range(len(dates)):  # Iterate through the dates by index
            date = dates[i]  # Get the date element at the current index
            dateValue = date.text
            print("Date : " + dateValue + " " + month + " " + year)
            selectDate(dateValue)
            time.sleep(2)
            slots = findAvailableSlots()
            for i in range(len(slots)):
                slot = slots[i]
                slotValue = slot.text
                slotTime, slotSeats = slotValue.split('\n')
                # Format the parts into the desired format
                # slotValue = f"Time : {slotTime} & Seats : {slotSeats}"
                print(f"Time : {slotTime} & Seats : {slotSeats}")
                slots = findAvailableSlots()
            print("\n")
            dates = findAvailableDates()
            
            
        

driver.quit()