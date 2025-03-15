import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(5)
driver.find_element(By.ID, "shopping_cart_container").click()
driver.find_element(By.ID, "checkout").click()
time.sleep(5)
driver.find_element(By.ID, "first-name").send_keys("Tosin")
driver.find_element(By.ID, "last-name").send_keys("williams")
driver.find_element(By.ID, "postal-code").send_keys("110241")
driver.find_element(By.ID, "continue").click()
time.sleep(5)
driver.find_element(By.ID, "finish").click()
driver.find_element(By.ID, "back-to-products").click()
time.sleep(5)