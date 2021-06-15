
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
time.sleep(1)
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
    try:
        driver.find_element_by_class_name("jobs-apply-button").click()
        #input telephone number
        telephone_number_input = driver.find_element_by_css_selector(".ph5 input")
        telephone_number_input.send_keys(telephone_number)
        #click next
        driver.find_element_by_css_selector("footer button").click()
        #choose cv step
        driver.find_elements_by_css_selector("footer button")[1].click()
        #untick follow on company
        driver.find_element_by_css_selector("footer label").click()
        #click submit application
        submit_button = driver.find_elements_by_css_selector("footer button")[1].click()

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            driver.find_element_by_css_selector("div button").click()
            driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary").click()

        else:
            submit_button.click()
            # click eyeball to hide job
            driver.find_element_by_css_selector(".job-card-container__action-container li-icon").click()

    except NoSuchElementException:
        print("No such element found. Skipped")




