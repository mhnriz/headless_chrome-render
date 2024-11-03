from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import subprocess

# Check Chrome binary path
chrome_path = "/usr/bin/google-chrome"
result = subprocess.run(["which", "google-chrome"], capture_output=True, text=True)
if result.stdout.strip():
    chrome_path = result.stdout.strip()

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")

# Start Chrome with Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://example.com")
    print("Page title:", driver.title)

finally:
    driver.quit()
