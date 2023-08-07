from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestLogin:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_search_existing_school(self, driver):
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

        driver.find_element(By.ID, "search-jobs").clear()
        time.sleep(3)
        driver.find_element(By.ID, "search-jobs").send_keys("Zamit Future School")
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/aside[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(5)

    def test_search_non_existing_school(self, driver):
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

        driver.find_element(By.ID, "search-jobs").clear()
        time.sleep(3)
        driver.find_element(By.ID, "search-jobs").send_keys("St. John school , Jaipur")
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/aside[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(5)

        error_message = driver.find_element(By.XPATH, "//strong[contains(text(), 'Record not found')]").text
        assert 'Record not found' in error_message
        #
        # def test_board_filters(self, setup):
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #     time.sleep(3)
        #     assert "checked Board - A LEVEL Filters" in self.driver.page_source
        #     print("Test Passed")
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #     time.sleep(3)
        #     assert "Unchecked Board - A LEVEL Filters" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'CBSE')]").click()
        #     time.sleep(3)
        #     assert "checked CBSE un checked" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'CBSE')]").click()
        #     time.sleep(3)
        #     assert "Unchecked CBSE un checked" in self.driver.page_source
        #
        # # Similar test methods for other filters can be added here
        #
        # def test_apply_filters(self, setup):
        #     self.driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
        #     time.sleep(6)
        #
        #     assert "Test Passed" in self.driver.page_source
        #
        # # Add more test methods as needed
        #
        # def test_work_experience_filters(self, setup):
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #     time.sleep(3)
        #     assert "checked Work Experience - 0--1 years Filters" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #     time.sleep(3)
        #     assert "Unchecked Work Experience - 0--1 years Filters" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'1-5 years')]").click()
        #     time.sleep(3)
        #     assert "checked Work Experience - 1-5 years Filters" in self.driver.page_source
        #
        #     # Add more work experience filters here
        #
        # def test_subjects_filters(self, setup):
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #     time.sleep(3)
        #     assert "checked Subjects | Accountancy|  Filters" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #     time.sleep(3)
        #     assert "Unchecked Subjects | Accountancy|  Filters" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'Art')]").click()
        #     time.sleep(3)
        #     assert "checked Subjects | Art|  Filters" in self.driver.page_source
        #
        #     # Add more subjects filters here
        #
        # def test_teaching_level_filters(self, setup):
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'PPRT')]").click()
        #     time.sleep(3)
        #     assert "Unchecked Teaching Level | PPRT|  Filters" in self.driver.page_source
        #
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'Others')]").click()
        #     time.sleep(3)
        #     assert "checked Teaching Level | Others|  Filters" in self.driver.page_source
        #
        #     # Add more teaching level filters here
        #
        # def test_publish_date_filter(self, setup):
        #     self.driver.find_element(By.XPATH, "//label[contains(text(),'Publish Date')]").click()
        #     time.sleep(3)
        #     assert "checked Publish Date |  Filters" in self.driver.page_source
        #
        #     # Add more publish date filter tests here
        #
        # # ... (other test methods)
        #
        #     # ... (previous test methods)
        #
        #     def test_teaching_level_filters(self, setup):
        #         # ... (previous test methods)
        #
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'Others')]").click()
        #         time.sleep(3)
        #         assert "checked Teaching Level | Others|  Filters" in self.driver.page_source
        #
        #         # Add more teaching level filters here
        #
        #     def test_publish_date_filter(self, setup):
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'Publish Date')]").click()
        #         time.sleep(3)
        #         assert "checked Publish Date |  Filters" in self.driver.page_source
        #
        #         # Add more publish date filter tests here
        #
        #     def test_combined_filters(self, setup):
        #         # Apply a combination of filters and test the results
        #         # Example: Apply Board filter, Work Experience filter, Subjects filter, and Teaching Level filter
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'PPRT')]").click()
        #         self.driver.find_element(By.XPATH, "//label[contains(text(),'Publish Date')]").click()
        #         self.driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
        #         time.sleep(6)
        #
        #         # ... (previous test methods)
        #
        #         def test_multiple_filter_combinations(self, setup):
        #             # Apply different combinations of filters and test the results
        #             # Example: Apply Board, Work Experience, and Subjects filters
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #             self.driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
        #             time.sleep(6)
        #
        #             # Add assertions to check the results based on the applied filters
        #
        #             # Apply different combination of filters
        #             # ...
        #
        #         def test_clear_filters(self, setup):
        #             # Apply a combination of filters and then clear them
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'PPRT')]").click()
        #             self.driver.find_element(By.XPATH, "//label[contains(text(),'Publish Date')]").click()
        #
        #             # Clear all filters
        #             self.driver.find_element(By.XPATH, "//a[contains(text(),'Clear All')]").click()
        #             time.sleep(6)
        #
        #             # ... (previous test methods)
        #
        #             def test_multiple_filter_combinations(self, setup):
        #                 # Apply different combinations of filters and test the results
        #                 # Example: Apply Board, Work Experience, and Subjects filters
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #                 self.driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
        #                 time.sleep(6)
        #
        #                 # Add assertions to check the results based on the applied filters
        #
        #                 # Apply different combination of filters
        #                 # ...
        #
        #             def test_clear_filters(self, setup):
        #                 # Apply a combination of filters and then clear them
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'A LEVEL')]").click()
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'0-1 years')]").click()
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'Accountancy')]").click()
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'PPRT')]").click()
        #                 self.driver.find_element(By.XPATH, "//label[contains(text(),'Publish Date')]").click()
        #
        #                 # Clear all filters
        #                 self.driver.find_element(By.XPATH, "//a[contains(text(),'Clear All')]").click()
        #                 time.sleep(6)
        #
        #                 # Add assertions to ensure filters are cleared and default state is reached
        #
        #             def test_back_to_search_results(self, setup):
        #
        #         # Apply filters and navigate back to search results
        #         # ...
        #
        #         # Add more test methods for different scenarios
        #
        #         # ... (other test methods)
        #
        #         # Add assertions to ensure filters are cleared and default state is reached
        #
        #         def test_back_to_search_results(self, setup):
        #     # Apply filters and navigate back to search results
        #     # ...
        #
        #     # Add more test methods for different scenarios
        #
        #     # ... (other test methods)
        #
        #
