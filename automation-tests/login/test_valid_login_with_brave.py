from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up options for Brave
options = Options()
options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'  # Path to Brave

# Use Service with ChromeDriver and initialize WebDriver
service = Service(ChromeDriverManager().install())  # Automatically installs the correct ChromeDriver version
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get('https://practicetestautomation.com/practice-test-login/')

# Find the username field and enter valid username
username_field = driver.find_element(By.ID, 'username')
username_field.send_keys('student')

# Find the password field and enter valid password
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('Password123')

# Click the Submit button
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

# Wait for a few seconds to allow the page to load (this can be improved with WebDriverWait)
time.sleep(3)

# Check if the page redirected successfully
if driver.current_url == 'https://practicetestautomation.com/logged-in-successfully/':
    print("Login successful!")
else:
    print("Login failed or did not redirect as expected.")

# Close the browser
driver.quit()
