from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Brave options
options = Options()
options.binary_location = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_argument("--start-maximized")

# Set up the ChromeDriver Service
service = Service(ChromeDriverManager().install())

# Launch Brave with ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(1)

    # Enter invalid username and valid password
    driver.find_element(By.ID, "username").send_keys("wrongUser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(1)

    # Check for the error message
    error_element = driver.find_element(By.ID, "error")
    assert "Your username is invalid!" in error_element.text

    print("✅ Test Passed: Correct error displayed for invalid username.")

except Exception as e:
    print(f"❌ Test Failed: {e}")

finally:
    driver.quit()
