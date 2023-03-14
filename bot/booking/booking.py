from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time

import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        self.currency = currency
        change_currency_button = self.find_element(By.CLASS_NAME,"e57ffa4eb5")
        change_currency_button.click()
        try:
            curr_button = self.find_element(By.XPATH, f"//DIV[@class=' ea1163d21f'][text()='{self.currency}']")
            curr_button.click()
        except:
            print("Currency not found")   


    def select_place_to_go(self, place=None):
        self.place = place
        place_field = self.find_element(By.NAME, "ss")
        place_field.send_keys(self.place)

    def select_dates_to_go(self, start_day, end_day):
        self.start_day = start_day
        self.end_day = end_day

        # Button to select dates
        select_days_buttons = self.find_element(By.XPATH, '//div[contains(@data-testid, "searchbox-dates-container")]')
        select_days_buttons.click()

        # Start date
        start_date_button = self.find_element(By.XPATH, f'//span[contains(@data-date, "{self.start_day}")]')
        start_date_button.click()

        # End date
        end_date_button = self.find_element(By.XPATH, f'//span[contains(@data-date, "{self.end_day}")]')
        end_date_button.click()

        search_button = self.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[4]/button/span')
        search_button.click()

        time.sleep(10)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

