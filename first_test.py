import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# variable declaration
wait = 5
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
first_name = "Tosin"
last_name = "williams"
postal_code = "110241"


# Browser initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

# Login details
UserName = driver.find_element(By.ID, "user-name")
UserName.send_keys(username)

PassWord = driver.find_element(By.ID, "password")
PassWord.send_keys(password)

Login = driver.find_element(By.ID, "login-button")
Login.click()

# Add to cart
BackPack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
BackPack.click()

BikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
BikeLight.click()

T_Shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
T_Shirt.click()

Fleece_Jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
Fleece_Jacket.click()

Onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
Onesie.click()

T_Shirt_Red = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
T_Shirt_Red.click()

time.sleep(wait)

# Go to checkout
driver.find_element(By.ID, "shopping_cart_container").click()
driver.find_element(By.ID, "checkout").click()
time.sleep(wait)

# Input checkout details
driver.find_element(By.ID, "first-name").send_keys(first_name)
driver.find_element(By.ID, "last-name").send_keys(last_name)
driver.find_element(By.ID, "postal-code").send_keys(postal_code)
driver.find_element(By.ID, "continue").click()
time.sleep(wait)

# Navigate to products
driver.find_element(By.ID, "finish").click()
driver.find_element(By.ID, "back-to-products").click()
time.sleep(wait)
