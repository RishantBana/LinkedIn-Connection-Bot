from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def login(driver, username_input, password_input):
    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys(username_input)

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password_input)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()
    except Exception as e:
        print(f"Error during login: {str(e)}")
        driver.quit()

def open_network_page(driver):
    try:
        my_network_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'mynetwork')]"))
        )
        my_network_tab.click()
    except Exception as e:
        print(f"Error opening network page: {str(e)}")
        driver.quit()

def send_connection_requests(driver, request_count):
    for i in range(request_count):
        try:
            connect_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Connect']"))
            )
            connect_button.click()
            print(f"Connection request {i + 1} sent successfully")

            time.sleep(random.uniform(2, 5))  
        except Exception as e:
            print(f"Error sending connection request {i + 1}: {str(e)}")
            time.sleep(random.uniform(2, 5))  

def main():
    linkedin_url = "https://www.linkedin.com/login"
    driver_path = 'C:\\Users\\admin\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

    username_input = ("your username/email")
    password_input = ("your password")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(linkedin_url)

    try:
        driver.get(linkedin_url)

        login(driver, username_input, password_input)
        open_network_page(driver)

        request_count = int(input("Enter number of requests to send: "))
        send_connection_requests(driver, request_count)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
