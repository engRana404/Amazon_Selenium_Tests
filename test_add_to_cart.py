'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (Firefox in this example)
driver = webdriver.Chrome()

# Navigate to Amazon.eg
driver.get("https://www.amazon.com/")

# Click on All tab
all_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "nav-hamburger-menu"))
)
all_tab.click()

# Go to Today’s Deals
todays_deals = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-csa-c-content-id='nav_cs_gb']"))
    )
driver.execute_script("arguments[0].scrollIntoView(true);", todays_deals)  # Scroll into view if necessary
driver.execute_script("arguments[0].click();", todays_deals)  # Click using JavaScript

back_to_school = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Back to School']"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", back_to_school)  # Scroll into view if necessary
driver.execute_script("arguments[0].click();", back_to_school)  # Click using JavaScript

# Click on the 1st product in the "Back to School" category

first_product = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='a-section a-spacing-none tallCellView gridColumn3 singleCell'])[1]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", first_product)  # Scroll into view if necessary
driver.execute_script("arguments[0].click();", first_product)  # Click using JavaScript


# Click on 2nd item in this product
second_item = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@data-component-type='s-search-result'])[2]"))
)
second_item.click()

# Add the item to cart with Qty = 2
quantity_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "quantity"))
)
quantity_dropdown.click()

quantity_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//option[@value='2']"))
)
quantity_option.click()

add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
)
add_to_cart_button.click()

# Go to cart
cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "nav-cart"))
)
cart.click()

# Verify correct items are added to the cart (name, price, qty, and subtotal)
# Replace the following XPATHs with the appropriate ones based on the page structure

item_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']"))
).text

item_price = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
).text

item_qty = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='a-dropdown-prompt']"))
).text

item_subtotal = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@id='sc-subtotal-amount-activecart']"))
).text

# Perform assertions
assert item_name == "Expected Item Name"
assert item_price == "Expected Price"
assert item_qty == "2"
assert item_subtotal == "Expected Subtotal"

# Close the browser
driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (ensure the correct path to your WebDriver is set)
driver = webdriver.Chrome()

# Explicit wait for elements
wait = WebDriverWait(driver, 10)

try:
    # 1. Navigate to Amazon.eg
    driver.get("https://www.amazon.com/")
    
    # 2. Click on All Tab
    all_tab = wait.until(EC.element_to_be_clickable((By.ID, "nav-hamburger-menu")))
    all_tab.click()
    
    # 3. Go to Today's Deals
    todays_deals = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-csa-c-content-id='nav_cs_gb']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", todays_deals)
    driver.execute_script("arguments[0].click();", todays_deals)
    
    # 4. Click on the 2nd Category
    second_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='widgetContent']//div[2]//a")))
    second_category.click()
    
    # 5. Click on the 1st Product in this Category
    first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='widgetContent']//div[1]//a")))
    first_product.click()
    
    # 6. Click on the 2nd Item in this Product
    second_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='variation_color_name']//ul/li[2]")))
    second_item.click()
    
    # 7. Add Item to Cart with Qty = 2
    quantity_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "quantity")))
    quantity_dropdown.send_keys("2")
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    
    # Handle any pop-ups if necessary
    # Example: no_thanks_button = driver.find_element(By.ID, "no-thanks")
    # if no_thanks_button.is_displayed():
    #     no_thanks_button.click()
    
    # 8. Go to Cart
    cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
    cart_button.click()
    
    # 9. Verify Name, Price, Quantity, and Subtotal
    cart_item_name = driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']")
    cart_item_price = driver.find_element(By.XPATH, "//span[@class='sc-product-price']")
    cart_item_quantity = driver.find_element(By.XPATH, "//span[@class='sc-product-quantity']")
    cart_item_subtotal = driver.find_element(By.XPATH, "//span[@class='sc-product-subtotal']")
    
    # Add assertions to verify these values
    assert "Expected Item Name" in cart_item_name.text
    assert cart_item_price.text == "Expected Price"
    assert cart_item_quantity.text == "2"
    assert cart_item_subtotal.text == "Expected Subtotal"
    
finally:
    # Close the browser
    driver.quit()

