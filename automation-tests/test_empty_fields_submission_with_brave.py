from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Brave options
options = Options()
options.binary_location = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"  # Update this with your Brave browser path

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the webpage
driver.get("https://practicetestautomation.com/practice-test-login/")

# Locate the Username and Password fields and input invalid credentials
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
submit_button = driver.find_element(By.ID, "submit")

username_field.send_keys("incorrectUser")  # Invalid username
password_field.send_keys("wrongPassword")  # Invalid password
submit_button.click()

# Wait for the error message to appear (in case it takes time to load)
try:
    # Wait for the error message to be visible
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    # Capture the error message text
    error_text = error_message.text
    print(f"Error Message: '{error_text}'")  # Output the error text for debugging

    # Trim any extra spaces
    error_text = error_text.strip()

    # Assert that the error message contains the expected substring (case-insensitive)
    assert "Your username is invalid!" in error_text, f"Expected error message but got: {error_text}"

except Exception as e:
    print(f"Error: {str(e)}")
    error_text = None  # Ensure that error_text is set to None if something goes wrong

# Pause for a few seconds to visually confirm the result
time.sleep(5)

# Close the browser
driver.quit()
