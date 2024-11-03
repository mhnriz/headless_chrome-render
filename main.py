from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import subprocess

# Check Chromium binary path
chromium_path = "/usr/bin/chromium-browser"
result = subprocess.run(["which", "chromium-browser"], capture_output=True, text=True)
if result.stdout.strip():
    chromium_path = result.stdout.strip()

# Set up Chromium options for Selenium
chrome_options = Options()
chrome_options.binary_location = chromium_path
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")

# Initialize the Selenium WebDriver with Chromium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open a webpage
    driver.get("https://example.com")
    print("Page title:", driver.title)

finally:
    driver.quit()
