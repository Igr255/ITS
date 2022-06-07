from selenium.webdriver.common.by import By
import uuid
import time

# helper script to help generate random methods/tools/test cases
# tool creation is not used as i had a problem with the webpage malfunctioning and
# not being able to see created tools in method relations


def fill_out_method(driver):
    methodName = "preMadeMethod" + uuid.uuid4().hex

    driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(methodName)
    driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("preMadeMethod purpose")

    # next 3 parts nest into iframe HTMLs and locates input named as "tinymce" and then nests back into main HTML
    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-method_description\"]/div/div/div[2]/iframe"))
    driver.find_element(By.ID, "tinymce").send_keys("Very nice description")
    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-method_strengths\"]/div/div/div[2]/iframe"))
    driver.find_element(By.ID, "tinymce").send_keys("Very nice strengths")
    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-method_limitations\"]/div/div/div[2]/iframe"))
    driver.find_element(By.ID, "tinymce").send_keys("Very bad limitations")
    driver.switch_to.default_content()

    # scrolls to the bottom of the page where the save button is located
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # saves the method
    driver.find_element(By.ID, "form-buttons-save").click()

    return methodName


def fill_out_tool(driver):
    toolName = "preMadeTool" + uuid.uuid4().hex

    driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys(toolName)
    driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("none")

    # next 3 parts nest into iframe HTMLs and locates input named as "tinymce" and then nests back into main HTML
    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-tool_description\"]/div/div/div[2]/iframe"))
    driver.find_element(By.ID, "tinymce").send_keys("Never gonna give you up")
    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-tool_strengths\"]/div/div/div[2]/iframe"))
    driver.find_element(By.ID, "tinymce").send_keys("Never gonna let you down")
    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id=\"formfield-form-widgets-tool_limitations\"]/div/div/div[2]/iframe"))
    driver.find_element(By.ID, "tinymce").send_keys("Never gonna run around and desert you")
    driver.switch_to.default_content()

    # scrolls to the bottom of the page where the save button is located
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(By.ID, "form-buttons-save").click()

    return toolName


def fill_out_test_case(driver):
    testCaseName = "preMadeTestCase" + uuid.uuid4().hex

    driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys(testCaseName)
    driver.find_element(By.ID, "form-widgets-test_case_id").send_keys(testCaseName)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(By.ID, "form-buttons-save").click()

    return testCaseName


def delete_checked_files(checkBoxes, driver):
    # if checkbox was found
    if len(checkBoxes) > 0:
        for item in checkBoxes:
            item.click()

        driver.find_element(By.ID, "btn-delete").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = driver.find_elements(By.XPATH, "//*[text()=\"Yes \"]")

        # if button is clickable
        if len(button) == 1:
            button[0].click()


def delete_used_files(driver, searched_text):

    # checking if producent is not already logged in
    res = driver.find_elements(By.ID, "portal-personaltools")

    if len(res) == 0:
        # login
        driver.find_element(By.ID, "personaltools-login").click()
        time.sleep(3)
        driver.find_element(By.ID, "__ac_name").send_keys("administrator")
        driver.find_element(By.ID, "__ac_password").send_keys("administrator")
        driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()

    driver.get('http://localhost:8080/repo/folder_contents')
    time.sleep(2)

    # apply filter
    driver.find_element(By.ID, "textFilterInput").send_keys(searched_text)

    # wait for items to load
    time.sleep(2)
    checkBoxes = driver.find_elements(By.ID, "selectAllInputCheckbox")
    delete_checked_files(checkBoxes, driver)

    # do the same for methods folder
    driver.get('http://localhost:8080/repo/method/folder_contents')
    time.sleep(2)

    # apply filter
    driver.find_element(By.ID, "textFilterInput").send_keys(searched_text)

    # wait for items to load
    time.sleep(2)
    checkBoxes = driver.find_elements(By.ID, "selectAllInputCheckbox")
    delete_checked_files(checkBoxes, driver)

