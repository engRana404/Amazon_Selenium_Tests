from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver Chrome
driver = webdriver.Chrome()

try:
    # Navigate to Amazon
    driver.get('https://www.amazon.eg/-/en/')
    
    # Click on the sign-in button
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-link-accountList"))
    )
    sign_in_button.click()

    # Enter an unregistered email
    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ap_email"))
    )
    email_field.send_keys("unregistered_email@example.com")  # Use an unregistered email

    # Click on Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Wait for the error message
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-alert-heading"))
    )
    print("Actual Error Message:", error_message.text)

    # Check the error message text
    if "There was a problem" in error_message.text:
        print("Test Passed: User cannot log in with a valid but unregistered email.")
    else:
        print("Test Failed: The error message is not as expected.")
        driver.save_screenshot("test_login.png")
    

finally:
    # Close the browser
    time.sleep(5)  # Optional: just to observe the result before closing
    driver.quit()
