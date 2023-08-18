url = "YOUR_WEBSITE_URL_HERE"
driver.get(url)

# Locate the username and password fields and enter values
username_field = driver.find_element_by_id("MainContent_LoginUser_UserName")
password_field = driver.find_element_by_id("MainContent_LoginUser_Password")

# Replace "your_username" and "your_password" with the actual values
username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Locate the login button and click it
login_button = driver.find_element_by_id("MainContent_LoginUser_LoginButton")
login_button.click()

closing_prices_button = driver.find_element(By.XPATH, "//a[contains(@href, 'closing-prices')]")
actions = ActionChains(driver)
actions.click(closing_prices_button).perform()

export_button = driver.find_element(By.ID, "MainContent_MainContent_ExportButton")
export_button.click()

# Switch to the pop-up iframe
iframe = driver.find_element(By.XPATH, "//iframe[contains(@name, 'confirm')]")
driver.switch_to.frame(iframe)

# Locate and click the "OK" button in the pop-up
ok_button = driver.find_element(By.XPATH, "//a[@class='rwPopupButton' and contains(text(), 'OK')]")
ok_button.click()

# Switch back to the main content
driver.switch_to.default_content()