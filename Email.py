# Program to Send Email using Selenium

from selenium import webdriver
import time

em = input("Enter Email Id: ")
ps = input("Enter Password: ")
re = input("Enter Recipient Email: ")
su = input("Enter Subject: ")
bo = input("Enter Message: ")

driver = webdriver.Chrome('C:/Users/hp/Desktop/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://gmail.com")

email_id = driver.find_element_by_class_name("whsOnd")
email_id.send_keys(em)
btn1 = driver.find_element_by_class_name("RveJvd")
btn1.click()

time.sleep(4)

password = driver.find_element_by_class_name("whsOnd")
password.send_keys(ps)
btn2 = driver.find_element_by_class_name("RveJvd")
btn2.click()

time.sleep(20)

compose = driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3")
compose.click()

time.sleep(10)

recipients = driver.find_element_by_class_name("vO")
recipients.send_keys(re)

subject = driver.find_element_by_class_name("aoT")
subject.send_keys(su)

body = driver.find_element_by_class_name("Am")
body.send_keys(bo)

send = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")
send.click()

time.sleep(5)

print("******** Message Sent!!! ********")

driver.close()
driver.quit()

