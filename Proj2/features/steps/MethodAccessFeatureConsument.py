#!/usr/bin/env python3
import behave.runner
from behave import *
from features.steps.testHelper import *
import time

# keeping track of used methods
createdMethod = ""


@given(u'producent created a method')
def step_impl(context: behave.runner.Context):
    # login
    context.driver.find_element(By.ID, "personaltools-login").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
    context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()

    # add new method
    time.sleep(2)
    context.driver.find_element(By.ID, "plone-contentmenu-factories").click()
    context.driver.find_element(By.ID, "method").click()

    # fill methods required fields
    global createdMethod
    createdMethod = fill_out_method(context.driver)


@given(u'method created by producent is set to \'Published\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-publish").click()


@given(u'user is logged in as consument')
def step_impl(context):
    time.sleep(1)
    # logs out from producent account
    context.driver.find_element(By.ID, "portal-personaltools").click()
    context.driver.find_element(By.ID, "personaltools-logout").click()


@when(u'consument is on "Methods" page')
def step_impl(context):
    context.driver.get('http://localhost:8080/repo/method')


@then(u'consument can see the method being colored in green')
def step_impl(context):
    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    color = context.driver.find_element(By.XPATH, xpath).value_of_css_property('color')

    assert(color == "rgb(32, 71, 36)")


@given(u'method created by producent is set to \'Private\'')
def step_impl(context):
    # seeting it to public nad back to private to see if it changes correctly
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-publish").click()

    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-reject").click()


@then(u'consument cannot see the method')
def step_impl(context):
    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    retrieved_elements = context.driver.find_elements(By.XPATH, xpath)

    assert(len(retrieved_elements) == 0)


@given(u'method created by producent is set to \'Submit for publication\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-submit").click()
