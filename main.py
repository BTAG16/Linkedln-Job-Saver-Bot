import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException

from dotenv import load_dotenv

load_dotenv()

linkedin_url = "https://www.linkedin.com/jobs/search/"
email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1920, 1080)
driver.implicitly_wait(20)
driver.get(linkedin_url)

def safe_find_element(by, value, retries=5):
    for _ in range(retries):
        try:
            element = driver.find_element(by, value)
            return element
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            time.sleep(1)
    return None

try:
    sign_in = safe_find_element(By.XPATH,
                                '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    if sign_in:
        sign_in.click()
    else:
        raise NoSuchElementException("Sign-in button not found")

    email_entry = safe_find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
    passwd_entry = safe_find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')

    if email_entry and passwd_entry:
        email_entry.send_keys(email, Keys.TAB)
        passwd_entry.send_keys(password, Keys.ENTER)
    else:
        raise NoSuchElementException("Email or password input field not found")

    input("Please solve the CAPTCHA and press Enter to continue...")

    time.sleep(5)

    try:
        positions = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
        for job in positions:
            try:
                job.click()
                time.sleep(1)
                job_entry = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
                job_entry.click()
                time.sleep(1)
                follow_btn = driver.find_element(By.CSS_SELECTOR, value=".jobs-company__box div button")
                ActionChains(driver).move_to_element(follow_btn).click().perform()
                time.sleep(2)
            except StaleElementReferenceException:
                print("Encountered stale element, retrying...")
                continue
    except StaleElementReferenceException:
        print("Encountered stale element in job positions, retrying...")

finally:
    driver.quit()
    pass
