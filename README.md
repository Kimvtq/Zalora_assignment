## Zalora_assignment

# Question
The Business Excellence team would like to build an automated solution to automate a manual
scraping process in the Commercial department. The team has given you this task, and they
would like to see you demonstrate your abilities by automating the scraping of product media
(images and videos) for ZALORA SKUs on the ZALORA website.
The task for Question 1 is as follows:
● Write a script in Python to scrape all product media (images and video) for the SKUs
listed down in this file
● You are required to send us your script and the product media (result)
● The script must allow for all the SKU product media to be easily obtained for all the SKUs
without having to manually access or open the ZALORA website
● All media must be placed into different subfolders of SKUs, i.e. each subfolder must have
images and videos for only 1 SKU.
● For example, for this SKU (A3B30AAC6FF98CGS), based on the SKU’s product display
view (PDV), there are 4 product images and 1 video associated with this item. The script
must ensure that the 4 images and 1 video are automatically scraped (downloaded) into
a folder labelled “A3B30AAC6FF98CGS” in your PC, before scraping the product media
for the next SKU in the list.
● Please submit the code on a git repo, try to follow best practices as possible from writing
good commit messages, clean code, testing, having scalability in mind as well, provide
your suggested architecture and why you chose each component.

# To create the app

1. Download ChromeDriver and add to the project folder
 https://chromedriver.storage.googleapis.com/index.html?path=101.0.4951.41/
 
2. Put the file sku_list.xlsx to the project folder
 
2. Install libraries
	import requests: to scrape website content
	import os: to create new folders and direct 
	from selenium import webdriver: simulate user actions
	from selenium.webdriver.common.by import By: handle find elements in Selenium
	import openpyxl: to read data from .xlsx file
	
3. Step in code
	-	Read data from local excel file
	-	For each SKU, direct to the detailed page
	-	Get all the images and download to local folders
	

# To execute
Run the command: py .\main.py