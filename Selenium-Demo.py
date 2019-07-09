# Selenium Demo

from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/hp/Desktop/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

username = input("Enter Username: ")	# Admin
password = input("Enter Password: ")	# admin123

driver.find_element_by_id("txtUsername").send_keys(username)
driver.find_element_by_id("txtPassword").send_keys(password)
driver.find_element_by_id("btnLogin").click()

driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()

time.sleep(10)

driver.close()
driver.quit()

print("Done!")
