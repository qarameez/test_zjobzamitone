from selenium import webdriver
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
import allure_pytest



class Test_login1():
    def test_all(self,setup):
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


        driver.find_element(By.XPATH,"//a[contains(text(),'Post a Job')]").click()
        time.sleep(3)
        title = driver.title
        print(driver.title)
        assert title == "Add new Job | ZJobs", "Title mismatch"
        print("Test test_valid_login successfully executed")


        # Enter pot job page
        selectTeaching = Select(driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/select[1]"))
        selectTeaching.select_by_value("Others")
        time.sleep(2)
        print("Teaching Level")
        time.sleep(3)

        #Teaching Level
        driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/span[1]/span[1]/span[1]/ul[1]/li[1]/input[1]").click()
        time.sleep(2)

        #Subjects
        Subjects_art = driver.find_element(By.XPATH,
                            "//body/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/span[1]/span[1]/span[1]/ul[1]/li[1]/input[1]")
        time.sleep(2)
        Subjects_art.click()
        Subjects_art.send_keys("art")
        Subjects_art.send_keys(Keys.ENTER)

        #Languages
        time.sleep(2)
        Languages = driver.find_element(By.XPATH,
                            "//body/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/span[2]/span[1]/span[1]/ul[1]/li[1]/input[1]")
        time.sleep(2)
        Languages.click()
        Languages.send_keys("Hindi")
        Languages.send_keys(Keys.ENTER)
        time.sleep(3)

        # Enter selectExperience
        selectExperience = Select(driver.find_element(By.NAME,"work_experience"))
        selectExperience.select_by_value("1-5 years")
        time.sleep(2)
        print("selectExperience")
        time.sleep(3)

        # Enter Board
        selectBoard = Select(driver.find_element(By.NAME, "school_board"))
        time.sleep(2)
        selectBoard.select_by_value("ICSE")
        time.sleep(2)
        print("selectBoard")
        time.sleep(3)

        # Enter Gender
        selectGender = Select(driver.find_element(By.NAME,"gender"))
        print("selectGender")
        time.sleep(2)
        selectGender.select_by_value("male")
        print("Male")
        time.sleep(2)
        print("selectGender")
        time.sleep(3)



        # Enter AgeBracket
        selectAgeBracket = Select(driver.find_element(By.XPATH,"//body/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/select[7]"))
        selectAgeBracket.select_by_value("35 to 45 years")
        time.sleep(2)
        print("selectAgeBracket")
        time.sleep(3)

        #calender
        calender=driver.find_element(By.XPATH, "// input[ @ id = 'datepicker_new']")
        time.sleep(2)
        calender.click()
        calender.send_keys("31")
        calender.send_keys(Keys.ENTER)
        time.sleep(3)


        # School
        driver.find_element(By.ID,"schooladdress").click()
        time.sleep(2)
        driver.find_element(By.ID, "schooladdress").send_keys("Hello I am Rameez khan")
        time.sleep(5)

        # Enter Board
        selectBoard = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        selectBoard.select_by_value("11")
        time.sleep(5)
        print("selectState")
        time.sleep(3)

        # Enter City
        selectcity = Select(driver.find_element(By.NAME, "city"))
        selectcity.select_by_value("2635")
        time.sleep(2)
        print("selectcity")
        time.sleep(3)


        driver.find_element(By.XPATH, "//button[contains(text(),'Post')]").click()
        time.sleep(3)
        print("Update")

        # driver.find_element(By.ID, "upldLogoPopup").click()
        # print("upldLogoPopup")
        # time.sleep(3)

        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        alert.dismiss()
        time.sleep(3)


        driver.find_element(By.TAG_NAME,"button").click()
        time.sleep(3)
        print("All Done")