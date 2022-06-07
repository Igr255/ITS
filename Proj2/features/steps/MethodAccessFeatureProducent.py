#!/usr/bin/env python3
from behave import *
from features.steps.testHelper import *
import time

# keeping track of used methods
createdMethod = ""


@given(u'user is logged in as producent')
def step_impl(context):
    # checking if producent is not already logged in
    res = context.driver.find_elements(By.ID, "portal-personaltools")

    if len(res) == 0:
        # login
        context.driver.find_element(By.ID, "personaltools-login").click()
        context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
        context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@given(u'administrator created a method')
def step_impl(context):
    # add new method
    time.sleep(2)
    context.driver.find_element(By.ID, "plone-contentmenu-factories").click()
    context.driver.find_element(By.ID, "method").click()

    # fill methods required fields
    global createdMethod
    createdMethod = fill_out_method(context.driver)


@given(u'created method is set to \'Published\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-publish").click()


@when(u'producent is on "Methods" page')
def step_impl(context):
    context.driver.get('http://localhost:8080/repo/method')


@then(u'producent can see the method being colored in green')
def step_impl(context):
    global createdMethod
    # retrieving xpath based on method's name
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    color = context.driver.find_element(By.XPATH, xpath).value_of_css_property('color')

    # checking if color is correct
    assert(color == "rgb(32, 71, 36)")


@given(u'created method is set to \'Private\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-publish").click()

    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-reject").click()


@then(u'producent can see the method being colored in red')
def step_impl(context):
    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    color = context.driver.find_element(By.XPATH, xpath).value_of_css_property('color')

    assert(color == "rgb(196, 24, 60)")


@given(u'created method is set to \'Submit for publication\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-workflow").click()
    context.driver.find_element(By.ID, "workflow-transition-submit").click()


@then(u'producent can see the method being colored in yellow')
def step_impl(context):
    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    color = context.driver.find_element(By.XPATH, xpath).value_of_css_property('color')

    assert(color == "rgb(165, 169, 18)")

