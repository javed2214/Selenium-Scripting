# Whatsapp Message Sending Bot using Selenium
# Library Used: selenium and time

from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/hp/Desktop/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

fam = 'Y'

driver.get("https://web.whatsapp.com/")

print("Scan QR Code!")

while(fam != 'N'):

	x = int(input("\nEnter Number of Recipients: "))

	print("Enter Names: ")	# Case Sensitive

	nameList=[]

	for i in range(x):
		p = input()
		nameList.append(p)

	msg = input("Enter Message: ")
	count = int(input("Enter Count: "))

	for name in nameList:

		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()

		for i in range(count):
			msg_box = driver.find_element_by_class_name("_3u328").send_keys(msg)
			btn = driver.find_element_by_class_name("_3M-N-")
			btn.click()

	print("\n********** Message Sent!!! **********\n")

	fam = input("Press Y to Continue else Press N: ")

time.sleep(5)

driver.close()
driver.quit()
