from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")

# Load extension
extension_path = os.path.abspath('./extension')
chrome_options.add_argument(f"--load-extension={extension_path}")

# Start Chrome with Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open a webpage
    driver.get("https://example.com")
    time.sleep(5)  # Let the extension do its work

    # Interact with the page or the extension if needed
    print("Page title:", driver.title)

finally:
    driver.quit()
