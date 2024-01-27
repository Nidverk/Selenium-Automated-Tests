import pytest                                           #Nödvändiga importer.
from selenium import webdriver                          #Webdriver = browser automation framework.
from selenium.webdriver.support.select import Select    #Select är en class för att interagera med dropdown-element.
from selenium.webdriver.common.keys import Keys         #Keys är en class för att simulera tangenttryckningar.
from selenium.webdriver.common.by import By             #By lokaliserar element.
from selenium.webdriver.support.ui import WebDriverWait #Väntar på specifika conditions innan asserts/events
from selenium.webdriver.support import expected_conditions as EC #Väntar på specifika conditions innan testet fortlöper
import time                                             #Time module har funktioner kopplat till tid, timing m.m. används här för att pausa körningen i vissa test.


# Jira issue Ticket('ROV-10')
def test_user_can_navigate_to_saucedemo_page():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    WebDriverWait(driver, 10).until(
        EC.title_is("Swag Labs")
    )
    
    title = driver.title

    assert title == "Swag Labs"
    time.sleep(2)
    driver.quit()

# Jira issue Ticket('ROV-11')
def test_standard_user_can_login_using_correct_credentials():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()

    expected_url = "https://www.saucedemo.com/v1/inventory.html"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {driver.current_url}"  #f-string, särskild sträng som kan innehålla variabler eller expressions. Här byggs en sträng som innehåller både expected och current url
    cart_button = driver.find_element(by=By.ID, value="shopping_cart_container")
    assert cart_button.is_displayed()

    driver.quit()

# Jira issue ticket('ROV-12')
def test_standard_user_cannot_login_using_incorrect_credentials():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauze")
    time.sleep(2)
    
    login_button.click()
    error_message = driver.find_element(by=By.CLASS_NAME, value="error-button")
    assert error_message.is_displayed()
    
    time.sleep(2)

    error_message = driver.find_element(by=By.CLASS_NAME, value="error-button")
    assert error_message.is_displayed(), "Error message is not displayed."

    driver.quit()

# Jira issue ticket('ROV-13')
def test_standard_user_can_add_product_to_cart():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()
    
    addbackpacktocart_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn_primary.btn_inventory")
    addbackpacktocart_button.click()
    time.sleep(2)

    cart_button = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_container")
    cart_button.click()
    time.sleep(2)

    backpack_in_cart = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Sauce Labs Backpack')]")
    assert backpack_in_cart.is_displayed()

    driver.quit()

# Jira issue ticket('ROV-14')
def test_standard_user_when_logged_in_can_add_multiple_products_to_cart():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()

    addbackpacktocart_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn_primary.btn_inventory")
    addbackpacktocart_button.click()
    time.sleep(2)

    add_bike_light_to_cart_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn_primary.btn_inventory")
    add_bike_light_to_cart_button.click()
    time.sleep(2)
    
    cart_button = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_container")
    cart_button.click()
    
    time.sleep(2)
    
    backpack_in_cart = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Sauce Labs Backpack')]")
    assert backpack_in_cart.is_displayed()
    bikelight_in_cart = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Sauce Labs Bike Light')]")
    assert bikelight_in_cart.is_displayed()

    driver.quit()

# Jira issue ticket('ROV-15')
def test_locked_out_user_cannot_login_using_correct_credentials():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("locked_out_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()

    error_message = driver.find_element(by=By.CLASS_NAME, value="error-button")
    assert error_message.is_displayed()
    time.sleep(2)

    driver.quit()


# Jira isse ticket('ROV-16')
def test_problem_user_can_login_using_correct_credentials():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("problem_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()

    expected_url = "https://www.saucedemo.com/v1/inventory.html"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {driver.current_url}"
    cart_button = driver.find_element(by=By.ID, value="shopping_cart_container")
    assert cart_button.is_displayed()

    driver.quit()

# Jira issue ticket('ROV-17')
def test_problem_user_cannot_login_using_incorrect_credentials():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("problem_user")
    password_field.send_keys("secret_sauze")
    time.sleep(2)
    login_button.click()
    error_message = driver.find_element(by=By.CLASS_NAME, value="error-button")
    assert error_message.is_displayed()
    time.sleep(2)

    driver.quit()

# Jira issue ticket('ROV-18')
def test_problem_user_can_add_product_to_cart():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("problem_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()
    
    addbackpacktocart_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn_primary.btn_inventory")
    addbackpacktocart_button.click()
    time.sleep(2)

    cart_button = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_container")
    cart_button.click()
    time.sleep(2)

    backpack_in_cart = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Sauce Labs Backpack')]")
    assert backpack_in_cart.is_displayed()

    driver.quit()


# Jira issue ticket('ROV-20')
def test_problem_user_when_logged_in_can_add_multiple_products_to_cart():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("problem_user")
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    login_button.click()

    addbackpacktocart_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn_primary.btn_inventory")
    addbackpacktocart_button.click()
    time.sleep(2)

    add_bike_light_to_cart_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn_primary.btn_inventory")
    add_bike_light_to_cart_button.click()
    time.sleep(2)
    
    cart_button = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_container")
    cart_button.click()
    
    time.sleep(2)
    
    backpack_in_cart = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Sauce Labs Backpack')]")
    assert backpack_in_cart.is_displayed()
    bikelight_in_cart = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Sauce Labs Bike Light')]")
    assert bikelight_in_cart.is_displayed()

    driver.quit()

# Jira issue ticket('ROV-11')
def test_standard_user_can_login_using_correct_credentials_and_use_dropdown_filter_menu():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/v1/index.html")
    username_field = driver.find_element(by=By.ID, value="user-name")
    password_field = driver.find_element(by=By.ID, value="password")
    login_button = driver.find_element(by=By.ID, value="login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    dropdown_filter_menu = driver.find_element(by=By.CLASS_NAME, value="product_sort_container")

    selected_dropdown_text = "Name (Z to A)"

    dropdown_filter_menu.send_keys(Keys.ARROW_DOWN)
    dropdown_filter_menu.send_keys(Keys.ENTER)

    select = Select(dropdown_filter_menu)
    selected_visible_text = select.first_selected_option.text
    assert selected_visible_text == selected_dropdown_text
    time.sleep(2)

    driver.quit()