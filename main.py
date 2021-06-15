from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

linked_in_login = os.environ['LINKED_IN_LOGIN']
linked_in_password = os.environ['LINKED_IN_PASSWORD']
telephone_number = os.environ['TELEPHONE_NUMBER']

linked_in_login_endpoint = "https://www.linkedin.com/login"
linked_in_job_search_endpoint = "https://www.linkedin.com/jobs/search/?f_AL=true&f_JT=F&geoId=90009496&keywords=junior%20python%20developer&location=London%20Area%2C%20United%20Kingdom"

path_to_chrome_driver = r"C:\Users\Conan\Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path_to_chrome_driver)

driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get(linked_in_login_endpoint)
username_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")


username_input.send_keys(linked_in_login)
password_input.send_keys(linked_in_password)
password_input.send_keys(Keys.ENTER)

driver.get(linked_in_job_search_endpoint)

job_cards = driver.find_elements_by_css_selector(".job-card-container a")
for item in job_cards:
    item.click()
    time.sleep(2)
    driver.find_element_by_class_name("jobs-apply-button").click()
    telephone_number_input = driver.find_element_by_css_selector(".ph5 input")
    telephone_number_input.send_keys(telephone_number)
    driver.find_element_by_css_selector("footer button").click()
    # buttons = driver.find_elements_by_tag_name("button")
    # for button in buttons:
    #     if button.get_attribute("aria-label") == "Continue to next step":
    #         button.click()
print(len(job_cards))



