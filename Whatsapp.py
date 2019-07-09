# Whatsapp Message Sending Bot using Selenium
# Library Used: selenium and time

from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/hp/Desktop/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://web.whatsapp.com/")

print("Scan QR Code!")

name = input("Enter Name: ")
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg = input("Enter Message: ")

count = int(input("Enter Count: "))

for i in range(count):
	msg_box = driver.find_element_by_class_name("_3u328").send_keys(msg)
	btn = driver.find_element_by_class_name("_3M-N-")
	btn.click()

time.sleep(5)

driver.close()
driver.quit()

print("Message Sent!")

