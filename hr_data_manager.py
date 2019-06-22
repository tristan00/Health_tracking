import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scipy import stats
import time


garmin_connect_sign_in_url = 'https://connect.garmin.com/signin/'
user_name_id = 'username'
password_id = 'password'
sign_in_button_id = 'login-btn-signin'
health_stats_css = 'body > div.connect-container > nav > div > ul.main-nav-group.main > li:nth-child(2) > a > span'
all_day_hr_css = 'body > div.connect-container > nav > div > ul.main-nav-group.main > li.main-nav-item.open-main-nav-menu > ul > li:nth-child(4) > a'
gear_css = '#pageContainer > div > div.DailySummaryPage_headerContent__5RxH1 > div > div > div.flexboxgrid_col-xs-12__1qBu0.flexboxgrid_col-lg-8__2GN_e.flexboxgrid_collapse__OOU2Q > div > div.flexboxgrid_col-xs-3__3ojgO.flexboxgrid_col-md-4__1jqjd.flexboxgrid_collapse__OOU2Q > div:nth-child(2) > div.flexboxgrid_col-xs-12__1qBu0.flexboxgrid_collapse__OOU2Q.flexboxgrid_showAt-xs__tHwmF.flexboxgrid_showAt-sm__2c67f.flexboxgrid_showAt-md__5a-mB > div > div:nth-child(2) > div > button > i'
export_css = '#pageContainer > div > div.DailySummaryPage_headerContent__5RxH1 > div > div > div.flexboxgrid_col-xs-12__1qBu0.flexboxgrid_col-lg-8__2GN_e.flexboxgrid_collapse__OOU2Q > div > div.flexboxgrid_col-xs-3__3ojgO.flexboxgrid_col-md-4__1jqjd.flexboxgrid_collapse__OOU2Q > div:nth-child(2) > div.flexboxgrid_col-xs-12__1qBu0.flexboxgrid_collapse__OOU2Q.flexboxgrid_showAt-xs__tHwmF.flexboxgrid_showAt-sm__2c67f.flexboxgrid_showAt-md__5a-mB > div > div:nth-child(2) > div > div > div:nth-child(2)'
chrome_driver_path = r'C:\Users\trist\OneDrive\Desktop\hr_data_files\chromedriver.exe'


def sleep_random_amount(min_time = 1.0, max_time = 4.0, mu = None, sigma = 1.0, verbose= False):
    if not mu:
        mu = max_time - min_time

    var = stats.truncnorm(
    (min_time - mu) / sigma, (max_time - mu) / sigma, loc=mu, scale=sigma)
    sleep_time = var.rvs()
    if verbose:
        print('Sleeping for {0} seconds: {0}'.format(sleep_time))
    time.sleep(sleep_time)


# class WebDriver:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def __enter__(self):
#         return self.driver
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.driver.quit()


class HRDataManager():
    def __init__(self, ):
        with open('personal', 'r') as f:
            lines = f.readlines()
        self.user_name, self.password, self.data_file_loc, _ = lines[0].split('|')
        self.load_all_data()


    def load_all_data(self):
        # get collected data
        # if days are missing, try and scrape them
        pass


    def process_zip_files(self):
        pass
    

    def scrape_data(self):
        chrome_options = Options()
        chrome_options.add_argument("download.default_directory={}".format(self.data_file_loc))
        # chrome_options.add_argument("--headless")

        with webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options) as driver:
            driver.get(garmin_connect_sign_in_url)
            driver.refresh()
            # print(1)
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, user_name_id)))
            # print(2)
            #
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, password_id)))
            # print(3)
            #
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, sign_in_button_id)))
            # print(4)

            sleep_random_amount()

            driver.find_element_by_id(user_name_id).send_keys(self.user_name)
            sleep_random_amount()
            driver.find_element_by_id(password_id).send_keys(self.password)
            sleep_random_amount()
            driver.find_element_by_id(sign_in_button_id).click()
            sleep_random_amount()

            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, health_stats_css))).click()
            sleep_random_amount()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, all_day_hr_css))).click()
            sleep_random_amount()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, gear_css))).click()
            sleep_random_amount()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, export_css))).click()






if __name__ == '__main__':
    data_manager = HRDataManager()
    data_manager.scrape_data()