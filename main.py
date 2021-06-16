from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
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

job_cards = driver.find_elements_by_class_name("jobs-search-results__list-item")
print(len(job_cards))
for item in job_cards:
    time.sleep(1)
    item.click()
    time.sleep(2)
    try:
        driver.find_element_by_class_name("jobs-apply-button").click()
        #input telephone number
        telephone_number_input = driver.find_element_by_css_selector(".ph5 input")
        telephone_number_input.send_keys(telephone_number)

        if driver.find_element_by_css_selector("footer button").get_attribute("data-control-name") == "submit_unify":
            #unclick follow
            untick_checkbox = driver.find_elements_by_css_selector("footer label")
            if len(untick_checkbox) > 0:
                untick_checkbox[0].click()
            time.sleep(1)
            driver.find_element_by_css_selector("footer button").click()
            print(f"Applied for position")
            time.sleep(1)
            #circumvent popup
            buttons = driver.find_elements_by_class_name("artdeco-modal__dismiss")
            if len(buttons) == 1:
                buttons[0].click()

        #click next to proceed to cv section
        driver.find_element_by_css_selector("footer button").click()
        time.sleep(1)
        #click to proceed from cv section
        driver.find_elements_by_css_selector("footer button")[1].click()
        time.sleep(1)

        if driver.find_elements_by_css_selector("footer button")[1].get_attribute("data-control-name") != "submit_unify":
            driver.find_element_by_css_selector("div button").click()
            driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary").click()
        else:
            ##untick follow on company
            untick_checkbox = driver.find_elements_by_css_selector("footer label")
            if len(untick_checkbox) > 0:
                untick_checkbox[0].click()
            time.sleep(1)
            #click submit application
            driver.find_elements_by_css_selector("footer button")[1].click()
            print(f"Applied for position")
            # dismiss pop up window
            time.sleep(1)
            #circumvent popup
            buttons = driver.find_elements_by_class_name("artdeco-modal__dismiss")
            if len(buttons) == 1:
                buttons[0].click()
            time.sleep(1)


    except NoSuchElementException:
        print("No such element found. Skipped")




