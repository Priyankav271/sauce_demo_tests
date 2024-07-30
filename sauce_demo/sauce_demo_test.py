# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import time
#
#
# # Create a class for the tests
# class SauceDemoTest:
#     def __init__(self):
#         # Automatically download and set up the latest ChromeDriver
#         service = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=service)
#
#     def visit_login_page(self):
#         self.driver.get("https://www.saucedemo.com")
#
#     def successful_login(self, username, password):
#         self.driver.find_element(By.ID, "user-name").send_keys(username)
#         self.driver.find_element(By.ID, "password").send_keys(password)
#         self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
#         time.sleep(1)  # Wait for the page to load
#
#         # Verify we are on the main page
#         assert "Swag Labs" in self.driver.title, "Login failed, title did not match."
#
#         # Verify the app logo exists
#         assert self.driver.find_element(By.CLASS_NAME, "app_logo").is_displayed(), "App logo not found."
#
#     def failed_login(self, username, password):
#         self.driver.find_element(By.ID, "user-name").send_keys(username)
#         self.driver.find_element(By.ID, "password").send_keys(password)
#         self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
#         time.sleep(1)  # Wait for the error message to load
#
#         # Verify the error message
#         error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
#         assert "Epic sadface: Sorry, this user has been locked out." in error_message, "Error message did not match."
#
#     def order_product(self):
#         # Sort products from high to low price
#         self.driver.find_element(By.CLASS_NAME, "product_sort_container").click()
#         self.driver.find_element(By.XPATH, "//option[@value='hilo']").click()
#
#         # Add the highest priced product to the cart
#         self.driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
#
#         # Click on cart
#         self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#
#         # Click on checkout
#         self.driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
#
#         # Fill in checkout information
#         self.driver.find_element(By.ID, "first-name").send_keys("Alice")
#         self.driver.find_element(By.ID, "last-name").send_keys("Doe")
#         self.driver.find_element(By.ID, "postal-code").send_keys("592")
#         self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
#         time.sleep(1)  # Wait for the checkout overview page to load
#
#         # Verify the total amount
#         total_amount = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split()[-1]
#         assert total_amount == "$49.99", "Total amount did not match."
#
#         # Finish the order
#         self.driver.find_element(By.XPATH, "//button[@data-test='finish']").click()
#
#         time.sleep(10)  # Wait for the thank you message
#
#         # Verify the thank you message
#         assert "Thank you for your order!" in self.driver.page_source, "Thank you message not found."
#
#     def close_browser(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     test = SauceDemoTest()
#
#     # Scenario 1: Successful Login
#     test.visit_login_page()
#     test.successful_login("standard_user", "secret_sauce")
#
#     # Scenario 2: Failed Login
#     test.visit_login_page()
#     test.failed_login("locked_out_user", "secret_sauce")
#
#     # Scenario 3: Order a product
#     test.visit_login_page()
#     test.successful_login("standard_user", "secret_sauce")
#     test.order_product()
#
#     # Close the browser
#     test.close_browser()
