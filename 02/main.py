from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://the-internet.herokuapp.com/login"

# Open the URL
driver.get(url)

# Process to log in
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
login_button.click()

WebDriverWait(driver, 5).until(
    ec.text_to_be_present_in_element(
        (By.XPATH, '//*[@id="content"]/div/h4'),
        "Secure Area"
    )
)

# Example - How to avoid an element that not exists (see commented line)
try:
    # logout_button = driver.find_element(By.XPATH, 'asdasda')
    logout_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/a/i')
    logout_button.click()
except:
    print("Button not exist")

# REQUIRED ARGUMENT TO CLOSE CHROME DRIVER
driver.close()
