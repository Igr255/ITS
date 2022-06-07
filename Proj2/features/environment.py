#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
from features.steps.testHelper import *

# for some reason 'behave' command could not locate the environment script in the parent folder so i put it 
# in features/ as well just in case


def get_driver():
    """Get Firefox/Chrome driver from Selenium Hub"""

    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    driver.implicitly_wait(5)

    return driver


def before_all(context):
    context.driver = get_driver()
    context.driver.get('http://localhost:8080/repo')
    context.driver.fullscreen_window()


def after_all(context):
    context.driver.quit()


def after_feature(context, feature):
    delete_used_files(context.driver, "preMadeMethod")
    delete_used_files(context.driver, "preMadeTestCase")
