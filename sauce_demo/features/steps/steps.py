from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('I am on the Demo Login Page')
def step_given_login_page(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.saucedemo.com")

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def step_fill_standard_user(context):
    context.driver.find_element_by_id("user-name").send_keys("standard_user")
    context.driver.find_element_by_id("password").send_keys("secret_sauce")
    context.driver.find_element_by_xpath("//input[@type='submit']").click()

@then('I am redirected to the Demo Main Page')
def step_redirected_to_main_page(context):
    assert "Swag Labs" in context.driver.title

@then('I verify the App Logo exists')
def step_verify_logo_exists(context):
    logo = context.driver.find_element_by_class_name("app_logo")
    assert logo.is_displayed()

@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def step_fill_locked_out_user(context):
    context.driver.find_element_by_id("user-name").send_keys("locked_out_user")
    context.driver.find_element_by_id("password").send_keys("secret_sauce")
    context.driver.find_element_by_xpath("//input[@type='submit']").click()

@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def step_verify_error_message(context):
    error_message = context.driver.find_element_by_css_selector("h3[data-test='error']").text
    assert error_message == "Sorry, this user has been banned."

@given('I am on the inventory page')
def step_on_inventory_page(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")

@when('user sorts products from high price to low price')
def step_sort_products(context):
    dropdown = context.driver.find_element_by_css_selector("select.product_sort_container")
    dropdown.select_by_visible_text("Price (high to low)")

@when('user adds highest priced product')
def step_add_highest_priced_product(context):
    highest_price_product = context.driver.find_element_by_xpath("(//div[@class='inventory_item_price'])[1]/ancestor::div[@class='inventory_item']//button")
    highest_price_product.click()

@when('user clicks on cart')
def step_click_cart(context):
    context.driver.find_element_by_class_name("shopping_cart_link").click()

@when('user clicks on checkout')
def step_click_checkout(context):
    context.driver.find_element_by_xpath("//button[@data-test='checkout']").click()

@when('user enters first name Alice')
def step_enter_first_name(context):
    context.driver.find_element_by_id("first-name").send_keys("Alice")

@when('user enters last name Doe')
def step_enter_last_name(context):
    context.driver.find_element_by_id("last-name").send_keys("Doe")

@when('user enters zip code 592')
def step_enter_zip_code(context):
    context.driver.find_element_by_id("postal-code").send_keys("592")

@when('user clicks Continue button')
def step_click_continue(context):
    context.driver.find_element_by_xpath("//input[@type='submit']").click()

@then('I verify in Checkout overview page if the total amount for the added item is $49.99')
def step_verify_total_amount(context):
    total_amount = context.driver.find_element_by_css_selector(".summary_total_label").text
    assert total_amount == "Total: $49.99"

@when('user clicks Finish button')
def step_click_finish(context):
    context.driver.find_element_by_xpath("//button[@data-test='finish']").click()

@then('Thank You header is shown in Checkout Complete page')
def step_verify_thank_you_header(context):
    thank_you_header = context.driver.find_element_by_css_selector(".complete-header").text
    assert thank_you_header == "Thank you for your order!"

