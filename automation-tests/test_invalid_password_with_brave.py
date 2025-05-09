from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Configure Brave as the browser
brave_path = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
os.environ["BROWSER"] = "brave"

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument("--start-maximized")

# Initialize WebDriver with Brave and WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Locate and fill in username and incorrect password
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("wrongPassword")

# Click the Submit button
driver.find_element(By.ID, "submit").click()

# Wait briefly to observe result
time.sleep(2)

# Validate error message
error_message = driver.find_element(By.ID, "error").text
assert "Your password is invalid!" in error_message, "Error message not displayed or incorrect"

# Optional: print success for logging
print("Test Passed: Invalid password error message displayed correctly.")

# Close browser
driver.quit()
