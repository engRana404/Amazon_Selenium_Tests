from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start a new Chrome session
driver = webdriver.Chrome()

try: 
    # Go to Amazon Egypt website
    driver.get("https://www.amazon.eg/-/en/")

    # Click on the "All" tab
    all_tab = WebDriverWait(driver, 20).until( 
        EC.element_to_be_clickable((By.LINK_TEXT, "All")) 
    )
    all_tab.click()

    # Go to Today’s Deals
    todays_deals = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/ul[1]/li[17]/a"))
    )
    todays_deals.click()

    # Click on the 2nd category
    second_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[21]/div/div/div/div[2]/div[1]/div/div/div[2]/div/ol/li[2]/a")
    second_category.click()

    # Click on the 1st product in this category
    first_product = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/section/div/div/div[2]/div[2]/div/ol/li[1]/a/div/img")
    first_product.click()

    # Click on the 2nd item in this product
    second_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[9]/div[1]/ul/li[2]/div/div[3]/a/img"))
    )
    #second_item = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[9]/div[1]/ul/li[2]/div/div[3]/a/img")
    second_item.click()

    # Switch to the new window
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    # Click to open the quantity dropdown
    quantity_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "a-autoid-0-announce"))
    )
    quantity_dropdown.click()

    # Select quantity = 2 from the dropdown
    quantity_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='quantity_1']"))
    )
    quantity_option.click()

    # Add the item to cart
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
    )
    add_to_cart_button.click()
    
    # Go to cart
    cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nav-cart"))
    )
    cart.click()

    # Verify correct items are added to the cart (name, price, qty, and subtotal)
    item_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']"))
    ).text
    print(item_name)

    item_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
    ).text
    print(item_price)

    item_qty = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='a-dropdown-prompt']"))
    ).text
    print(item_qty)

    item_subtotal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@id='sc-subtotal-amount-activecart']"))
    ).text
    print(item_subtotal)

    time.sleep(5)  # Optional: just to observe the result before closing

    # Perform assertions
    assert item_name.startswith("Nagafa Shop")  
    assert item_price == "157."     
    assert item_qty == "2"
    assert "376.00" in item_subtotal

    print("Test passed: Item is added to the cart successfully.")
finally:
    driver.save_screenshot("test_add_to_cart.png")
    # Close the browser
    driver.quit()
