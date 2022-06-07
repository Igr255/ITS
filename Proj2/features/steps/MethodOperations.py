#!/usr/bin/env python3
from behave import *
from features.steps.testHelper import *
import time

createdMethod = ""


@given(u'producent account is logged in')
def step_impl(context):
    # checking if producent is not already logged in
    res = context.driver.find_elements(By.ID, "portal-personaltools")

    if len(res) == 0:
        # login
        context.driver.find_element(By.ID, "personaltools-login").click()
        context.driver.find_element(By.ID, "__ac_name").send_keys("administrator")
        context.driver.find_element(By.ID, "__ac_password").send_keys("administrator")
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@given(u'website is on "Add method" page')
def step_impl(context):
    # add new method
    time.sleep(2)
    context.driver.find_element(By.ID, "plone-contentmenu-factories").click()
    context.driver.find_element(By.ID, "method").click()


@given(u'required fields are not filled')
def step_impl(context):
    # fills random field that is not required
    context.driver.find_element(By.ID, "form-widgets-IBasic-description").send_keys("random summary that is not needed")


@when(u'producent saves the method')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'error is thrown')
def step_impl(context):
    # checks popup error
    time.sleep(2)
    errText = context.driver.find_element(By.CSS_SELECTOR, ".portalMessage > dd").text
    assert(errText == "There were some errors.")


@then(u'method is not created')
def step_impl(context):
    context.driver.get('http://localhost:8080/repo/method')


@then(u'method is not visible on methods page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    retrieved_elements = context.driver.find_elements(By.XPATH, xpath)

    assert(len(retrieved_elements) == 0)


@given(u'required fields are filled')
def step_impl(context):
    # creates a method with filled required fields
    methodName = "preMadeMethod" + uuid.uuid4().hex

    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(methodName)
    context.driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("preMadeMethod purpose")

    context.driver.switch_to.frame(
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-method_description\"]/div/div/div[2]/iframe"))
    context.driver.find_element(By.ID, "tinymce").send_keys("Very nice description")
    context.driver.switch_to.default_content()

    context.driver.switch_to.frame(
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-method_strengths\"]/div/div/div[2]/iframe"))
    context.driver.find_element(By.ID, "tinymce").send_keys("Very nice strengths")
    context.driver.switch_to.default_content()

    context.driver.switch_to.frame(
    context.driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-method_limitations\"]/div/div/div[2]/iframe"))
    context.driver.find_element(By.ID, "tinymce").send_keys("Very bad limitations")
    context.driver.switch_to.default_content()

    global createdMethod
    createdMethod = methodName


@then(u'method is created')
def step_impl(context):
    context.driver.get('http://localhost:8080/repo/method')


@then(u'method is visible on methods page')
def step_impl(context):
    # wait for methods to load
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    retrieved_elements = context.driver.find_elements(By.XPATH, xpath)

    print(createdMethod)
    print(len(retrieved_elements))

    assert (len(retrieved_elements) == 1)


@given(u'website is on existing method page')
def step_impl(context):

    # go to methods page
    context.driver.get('http://localhost:8080/repo')

    time.sleep(2)
    context.driver.find_element(By.ID, "plone-contentmenu-factories").click()
    context.driver.find_element(By.ID, "method").click()

    global createdMethod
    createdMethod = fill_out_method(context.driver)

    # go to methods page
    context.driver.get('http://localhost:8080/repo/method')

    # wait for methods to load
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # go to existing method
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    context.driver.find_element(By.XPATH, xpath).click()


@when(u'producent clicks on "Actions" button')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "plone-contentmenu-actions").click()


@when(u'producent clicks on "Delete" button')
def step_impl(context):
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()


@when(u'producent clicks on popup "Delete" button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > input:nth-child(1)").click()


@then(u'"Do you really want to delete this folder and all its contents?" popup should appear')
def step_impl(context):
    popupText = context.driver.find_element(By.CSS_SELECTOR, "h1.documentFirstHeading > span").text
    assert(popupText == "Do you really want to delete this folder and all its contents?")


@given(u'producent tries to remove a method')
def step_impl(context):
    pass


@given(u'"Do you really want to delete this folder and all its contents?" popup appeared')
def step_impl(context):
    popupText = context.driver.find_element(By.CSS_SELECTOR, "h1.documentFirstHeading > span").text
    assert(popupText == "Do you really want to delete this folder and all its contents?")


@then(u'method disappears from methods page')
def step_impl(context):

    # go to methods page
    context.driver.get('http://localhost:8080/repo/method')

    # wait for methods to load
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    retrieved_elements = context.driver.find_elements(By.XPATH, xpath)

    assert(len(retrieved_elements) == 0)


@when(u'producent edits the method')
def step_impl(context):
    context.driver.find_element(By.ID, "contentview-edit").click()


@when(u'producent edits methods data')
def step_impl(context):

    global createdMethod
    createdMethod += "veryNew"
    time.sleep(2)
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("veryNew")


@when(u'saves the edited method')
def step_impl(context):
    # wait for methods to load
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'"Changes saved" information appears')
def step_impl(context):
    time.sleep(2)
    errText = context.driver.find_element(By.CSS_SELECTOR, ".portalMessage").get_attribute('innerHTML')

    # for some reason the popupup has extra spaces all over the elements text
    assert("Changes saved" in errText)


@then(u'method gets updated')
def step_impl(context):
    # redundand step
    pass


@then(u'updated method is visible on methods page')
def step_impl(context):

    context.driver.get('http://localhost:8080/repo/method')
    # wait for methods to load
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    global createdMethod
    xpath = "//a[text()=\"{method}\"]".format(method=createdMethod)
    retrieved_elements = context.driver.find_elements(By.XPATH, xpath)

    assert (len(retrieved_elements) == 1)
