import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_valid_login(setup):
    driver = setup  # Using the fixture to get the driver instance
    driver.find_element(By.NAME, "email").send_keys("zamitfutureschool@gmail.com")
    driver.find_element(By.ID, "submit-login").click()
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("3APQAN")
    driver.find_element(By.ID, "submit-login").click()
    time.sleep(5)
    title = driver.title
    print(driver.title)
    assert title == "Jobs | ZJobs", "Title mismatch"
    print("Test test_valid_login successfully executed")

def test_invalid_password(setup):
    driver = setup  # Using the fixture to get the driver instance
    driver.find_element(By.NAME, "email").send_keys("zamitfutureschool@gmail.com")
    driver.find_element(By.ID, "submit-login").click()
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("3APQ6AN")
    driver.find_element(By.ID, "submit-login").click()
    time.sleep(5)
    title = driver.title
    print(driver.title)
    assert title == "Jobs | ZJobss", "Title mismatch"
    print("Test test_invalid_password successfully executed")
