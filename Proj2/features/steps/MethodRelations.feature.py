#!/usr/bin/env python3
from behave import *
from features.steps.testHelper import *
import time

createdMethod = ""
createdTool1 = ""
createdTool2 = ""
createdTestCase1 = ""
createdTestCase2 = ""


@given(u'producent is logged in')
def step_impl(context):
    # checking if producent is not already logged in
    res = context.driver.find_elements(By.ID, "portal-personaltools")

    if len(res) == 0:
        # login
        context.driver.find_element(By.ID, "personaltools-login").click()
        context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
        context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@given(u'method is created')
def step_impl(context):
    context.driver.get('http://localhost:8080/repo')
    time.sleep(2)

    # add new method
    context.driver.find_element(By.ID, "plone-contentmenu-factories").click()
    context.driver.find_element(By.ID, "method").click()

    # fill methods required fields
    global createdMethod
    createdMethod = fill_out_method(context.driver)


@given(u'two different test cases are created')
def step_impl(context):
    context.driver.get('http://localhost:8080/repo')
    time.sleep(2)

    # add new test case
    context.driver.find_element(By.ID, "plone-contentmenu-factories").click()
    context.driver.find_element(By.ID, "test_case").click()

    # fill test cases required fields
    global createdTestCase1
    createdTestCase1 = fill_out_test_case(context.driver)

    # create second test case
    context.driver.get('http://localhost:8080/repo/++add++test_case')
    time.sleep(2)

    # fill test cases required fields
    global createdTestCase2
    createdTestCase2 = fill_out_test_case(context.driver)


@given(u'method contains 0 relations with tools')
def step_impl(context):
    global createdMethod
    # go to existing method
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    context.driver.find_element(By.XPATH, xpath).click()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div > ul > li")
    assert(len(tools) == 0)


@when(u'producent edits method')
def step_impl(context):
    context.driver.find_element(By.ID, "contentview-edit").click()


@given(u'method contains 0 relations with test cases')
def step_impl(context):
    global createdMethod

    # go to methods page
    context.driver.get('http://localhost:8080/repo/method')
    # go to existing method
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    context.driver.find_element(By.XPATH, xpath).click()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div > ul > li")
    assert(len(tools) == 0)


@when(u'adds a test case relation')
def step_impl(context):
    # again switching to relations card and adding new test case
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-test_case_or_verification_and_validation_activity\"]/div/div[2]/ul/li/input").click()
    context.driver.find_element(By.CLASS_NAME, "pattern-relateditems-result-browse").click()
    context.driver.find_element(By.XPATH, "(//*[@class=\"pattern-relateditems-result-select selectable\"])[1]").click()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'on the method page there is 1 test case relation visible')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div > ul > li")
    assert(len(tools) == 1)


@given(u'method contains 1 relations with test cases')
def step_impl(context):
    global createdMethod

    # go to methods page
    context.driver.get('http://localhost:8080/repo/method')
    time.sleep(2)

    # go to existing method
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    context.driver.find_element(By.XPATH, xpath).click()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div > ul > li")
    assert(len(tools) == 1)


@when(u'producent removes a test case relation')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-test_case_or_verification_and_validation_activity\"]/div[2]/div[2]/ul/li[1]/a").click()

    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'on the method page there is 0 test case relations visible')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div > ul > li")
    assert(len(tools) == 0)


@given(u'method contains 0 relation with test cases')
def step_impl(context):
    global createdMethod

    # go to methods page
    context.driver.get('http://localhost:8080/repo/method')
    time.sleep(2)

    # go to existing method
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    context.driver.find_element(By.XPATH, xpath).click()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1)")
    assert(len(tools) == 0)


@when(u'adds two relations to a test case')
def step_impl(context):
    # switching to relations window
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()
    # clicking on test case realtions input
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-test_case_or_verification_and_validation_activity\"]/div/div[2]/ul/li/input").click()
    # nesting one directory up to fund test cases
    context.driver.find_element(By.CLASS_NAME, "pattern-relateditems-result-browse").click()
    # adding a test case
    context.driver.find_element(By.XPATH, "(//*[@class=\"pattern-relateditems-result-select selectable\"])[1]").click()

    # repeats cliking and adding a test case
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-test_case_or_verification_and_validation_activity\"]/div/div[2]/ul/li/input").click()
    context.driver.find_element(By.XPATH, "(//*[@class=\"pattern-relateditems-result-select selectable\"])[1]").click()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'on the method page there are 2 test cases relation visible')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    tools = context.driver.find_elements(
        By.CSS_SELECTOR, "#form-widgets-test_case_or_verification_and_validation_activity "
                         "> div > ul > li")

    assert(len(tools) == 2)
