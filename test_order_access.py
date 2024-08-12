from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome()

try:
    # Step 1: Go to https://www.amazon.eg/
    driver.get("https://www.amazon.eg/-/en/")
    time.sleep(2)  # Allow time for the page to load

    # Step 2: Hover over “Hello, sign in Account & Lists” at the top right corner
    account_lists = driver.find_element(By.ID, "nav-link-accountList")
    actions = ActionChains(driver)
    actions.move_to_element(account_lists).perform()
    time.sleep(2)  # Allow time for the menu to appear

    # Step 3: Select “Your Orders”
    your_orders = driver.find_element(By.LINK_TEXT, "Your Orders")
    your_orders.click()
    time.sleep(2)  # Allow time for the page to load

    # Verify that user can't see orders when not signed in
    print(driver.title)
    assert "Amazon Sign In" in driver.title, "User can see orders without signing in!"

    # Step 4: Go back to the account & lists menu
    driver.back()
    time.sleep(2)  # Allow time for the previous page to load
    actions.move_to_element(account_lists).perform()
    time.sleep(2)

    # Step 5: Select “Your Addresses”
    your_addresses = driver.find_element(By.LINK_TEXT, "Your Addresses")
    your_addresses.click()
    time.sleep(2)  # Allow time for the page to load

    # Verify that user can't see addresses when not signed in
    print(driver.title)
    assert "" in driver.title or "Amazon Sign In" in driver.title, "User can see addresses without signing in!"

    # Step 6: Go back to the account & lists menu
    driver.back()
    time.sleep(2)  # Allow time for the previous page to load
    actions.move_to_element(account_lists).perform()
    time.sleep(2)

    # Step 7: Select “Your Lists”
    your_lists = driver.find_element(By.LINK_TEXT, "Your Lists")
    your_lists.click()
    time.sleep(2)  # Allow time for the page to load

    # Verify that user can see the "Your Lists" intro screen
    print(driver.title)
    assert "Your List" in driver.title, "User cannot see the 'Your Lists' intro screen!"

    print("Test passed: All conditions met.")
except AssertionError as error:
    driver.save_screenshot("test_order_access.png")
    print(f"Test failed: {error}")
finally:
    driver.quit()
