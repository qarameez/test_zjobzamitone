from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
import allure_pytest

class Test_login1():
    def test_all(self):
        driver = webdriver.Chrome()
        driver.get("https://zjobsandbox.zamit.one/login")
        driver.maximize_window()
        driver.find_element(By.NAME, "email").send_keys("zamitfutureschool@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "submit-login").click()
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys("3APQAN")
        time.sleep(2)
        driver.find_element(By.ID, "submit-login").click()
        time.sleep(5)


        #check Enter school name
        driver.find_element(By.ID,"search-jobs").clear()
        time.sleep(3)
        driver.find_element(By.ID,"search-jobs").send_keys("Zamit Future School")
        time.sleep(3)
        driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/aside[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(5)
        print("pass")



        # check Enter school name
        driver.find_element(By.ID, "search-jobs").clear()
        time.sleep(3)
        driver.find_element(By.ID, "search-jobs").send_keys("gsdgdsfgdf")
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/aside[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(5)
        if 'Record not found' in driver.find_element(By.XPATH,"// strong[contains(text(), 'Record not found')]").text:
            assert True
        else:
            assert False
            print("all test pass")

        driver.find_element(By.ID, "search-jobs").clear()
        driver.find_element(By.XPATH,
                            "//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/aside[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(5)



        # Board - A LEVEL Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'A LEVEL')]")).click()
        time.sleep(3)
        print("checked Board - A LEVEL Filters")


        # # Board - CBSE Filters
        #  A LEVEL Filters un checked
        driver.find_element(By.XPATH, ("//label[contains(text(),'A LEVEL')]")).click()
        time.sleep(3)
        print("Unchecked Board - A LEVEL Filters")
        driver.find_element(By.XPATH, ("//label[contains(text(),'CBSE')]")).click()
        time.sleep(3)
        print("checked CBSE un checked")

        #  CBSE un checked
        driver.find_element(By.XPATH, ("//label[contains(text(),'CBSE')]")).click()
        time.sleep(3)
        print("Unchecked CBSE un checked")

        # Work Experience - 0--1 years Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'0-1 years')]")).click()
        time.sleep(3)
        print("checked Work Experience - 0--1 years Filters")

        # Work Experience - 0--1 years Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'0-1 years')]")).click()
        time.sleep(3)
        print("Unchecked Work Experience - 0--1 years Filters")

        # Work Experience - 1-5 years Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'1-5 years')]")).click()
        time.sleep(3)
        print("checked ork Experience - 1-5 years Filters")
        #
        # #  Work Experience - 1-5 years Filters
        # driver.find_element(By.XPATH, ("//label[contains(text(),'1-5 years')]")).click()
        # time.sleep(3)
        # print("Unchecked Work Experience - 1-5 years Filters")

        # Subjects | Accountancy|  Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'Accountancy')]")).click()
        time.sleep(3)
        print("checked Subjects | Accountancy|  Filters")
        #
        # #  Subjects | Accountancy|  Filters
        # driver.find_element(By.XPATH, ("//label[contains(text(),'Accountancy')]")).click()
        # time.sleep(3)
        # print("Unchecked Subjects | Accountancy|  Filters")

        # Subjects | Art|  Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'Art')]")).click()
        time.sleep(3)
        print("checked Subjects | Art|  Filters")

        #  Subjects | Accountancy|  Filters
        # driver.find_element(By.XPATH, ("//label[contains(text(),'Art')]")).click()
        # time.sleep(3)
        # print("Unchecked Subjects | Art|  Filters")

        # Teaching Level | PPRT|  Filters
        # driver.find_element(By.XPATH, ("//label[contains(text(),'PPRT')]")).click()
        # time.sleep(3)
        # print("checked Teaching Level | PPRT|  Filters")

        #  Teaching Level | PPRT|  Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'PPRT')]")).click()
        time.sleep(3)
        print("Unchecked Teaching Level | PPRT|  Filters")

        # Teaching Level | Others|  Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'Others')]")).click()
        time.sleep(3)
        print("checked Teaching Level | Others|  Filters")

        # #  Teaching Level | Others|  Filters
        # driver.find_element(By.XPATH, ("//label[contains(text(),'Others')]")).click()
        # time.sleep(3)
        # print("Unchecked Teaching Level | Others|  Filters")

        # Publish Date |  Filters
        driver.find_element(By.XPATH, ("//label[contains(text(),'Publish Date')]")).click()
        time.sleep(3)
        print("checked Publish Date |  Filters")
        #
        # #  Publish Date | |  Filters
        # driver.find_element(By.XPATH, ("//label[contains(text(),'Publish Date')]")).click()
        # time.sleep(3)
        # print("Unchecked Publish Date | |  Filters")


        driver.find_element(By.XPATH,"//button[contains(text(),'Update')]").click()
        time.sleep(6)

        print("Test Passed")

        # driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[1]").click()
        # time.sleep(3)
        # driver.back()
