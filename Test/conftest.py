from selenium import webdriver
import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
import allure_pytest


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://zjobsandbox.zamit.one/login")
    driver.maximize_window()
    yield driver  # The fixture should yield the driver so that tests can use it
    driver.quit()




