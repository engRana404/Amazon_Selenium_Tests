# Amazon_Selenium_Tests

## Overview

This project contains automated test scripts to verify several functionalities on the [Amazon Egypt](https://www.amazon.eg/-/en/) website. The tests are built using Selenium WebDriver and are designed to ensure the website's key features work as expected.

## Test Scenarios

### 1. Login Verification (`test_login.py`)
- **Objective**: Verify that a user cannot log in with a valid but unregistered email.
- **Details**:
  - Navigate to Amazon Egypt's login page.
  - Enter an unregistered email and attempt to log in.
  - Assert that the appropriate error message is displayed.
  - Save a screenshot on failure.

### 2. Order and Address Access Verification (`test_order_access.py`)
- **Objective**: Verify that a user cannot access "Your Orders" and "Your Addresses" without signing in, but can access the "Your Lists" intro screen.
- **Details**:
  - Hover over "Hello, sign in Account & Lists" and attempt to access "Your Orders" and "Your Addresses" without logging in.
  - Assert that the user is redirected to the sign-in page.
  - Verify that the "Your Lists" intro screen is accessible without logging in.
  - Save a screenshot on failure.

### 3. Add to Cart Verification (`test_add_to_cart.py`)
- **Objective**: Verify that items are correctly added to the cart, including name, price, quantity, and subtotal.
- **Details**:
  - Navigate to "Today's Deals" and select a product.
  - Add the product to the cart with a specific quantity.
  - Verify that the correct item name, price, quantity, and subtotal are displayed in the cart.
  - Save a screenshot on failure.

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver
- Chrome browser installed

### Installing Dependencies

Use the following command to install the necessary Python packages:

```bash
pip install selenium webdriver_manager
```

## Running the Tests

1. **Login Test**: 
    ```bash
    python test_login.py
    ```

2. **Order and Address Access Test**:
    ```bash
    python test_order_access.py
    ```

3. **Add to Cart Test**:
    ```bash
    python test_add_to_cart.py
    ```

## Results

Each test script prints the result of the test to the console. If a test fails, a screenshot of the failure will be saved in the same directory as the test script with the corresponding name (e.g., `test_login.png`, `test_order_access.png`, `test_add_to_cart.png`).
