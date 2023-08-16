from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# Create a new instance of the Chrome browser - TODO: Add the Chromedriver Address
driver = webdriver.Chrome()
download_directory = '/path/to/your/download/directory'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # May be needed depending on your environment
chrome_options.add_argument('--headless')    # Run in headless mode if desired
chrome_options.add_argument('--disable-gpu') # Disable GPU acceleration if needed

# Set the download directory option
chrome_options.add_argument(f'--download.default_directory={download_directory}')