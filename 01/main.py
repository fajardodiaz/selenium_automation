from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# New implementation for chrome driver - By a Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = "https://the-internet.herokuapp.com/dynamic_controls"

# Open the URL
driver.get(url)

# Process to test
button_remove = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
button_remove.click()

# TEST - Verify if the text exists
WebDriverWait(driver, 30).until(
    ec.text_to_be_present_in_element(
        (By.ID, "message"),  # Element filtration
        "It's gone!"  # Expected text
    )
)

# REQUIRED ARGUMENT TO CLOSE CHROME DRIVER
driver.close()
