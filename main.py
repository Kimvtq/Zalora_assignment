import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# define a method to create a new folder and direct to it
def create_a_folder(folder_name):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder_name))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder_name))

# define a method to get to detailed page of a SKU then download all images
def download_image(sku):
    # Direct to search result page for a sku
    driver.get("https://www.zalora.com.my/catalog/?q=" + sku)

    # Get the result and click on the link
    result_link = driver.find_element(By.XPATH,'//li[@id="' + sku + '"]//a')
    result_link.click()

    # Get current page / sku detailed page
    url = driver.current_url
    print(url)

    # Get all thumbnails except video 
    thumbnails  = driver.find_elements(By.XPATH,'//ul[contains(@class,"prd-moreImagesList")]//li[not(div)]')

    for thumbmail in thumbnails:
        thumbmail.click()
        img = driver.find_element(By.CSS_SELECTOR,'.prd-image')
        name = img.get_attribute("alt")
        link = img.get_attribute('src')
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)

# Initial driver
driver = webdriver.Chrome("ChromeDriver\chromedriver.exe")   
create_a_folder("media")

create_a_folder("8EFE6SH6649021GS")
download_image("8EFE6SH6649021GS")

     

