from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # May be needed depending on your environment
chrome_options.add_argument('--headless')    # Run in headless mode if desired
chrome_options.add_argument('--disable-gpu') # Disable GPU acceleration if needed
download_directory = '.'

# Set the download directory option
chrome_options.add_argument(f'--download.default_directory={download_directory}')
driver = webdriver.Chrome(options=chrome_options)

driver.quit()