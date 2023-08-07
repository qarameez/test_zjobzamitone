
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
import allure_pytest



class Test_login12():

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



        # Click on Edit button
        time.sleep(5)
        driver.find_element(By.XPATH,'//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/span[1]').click()
        time.sleep(3)
        driver.back()
        print("Click on Edit button")
        time.sleep(3)

        # Click on View button
        driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[1]").click()
        time.sleep(3)
        driver.back()
        print("Click on View button")
        time.sleep(3)

        # Click on View Applicant
        driver.find_element(By.XPATH,
                            "//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/a[1]/span[1]").click()
        time.sleep(3)
        driver.back()
        print("Click on View Applicant")
        time.sleep(3)

