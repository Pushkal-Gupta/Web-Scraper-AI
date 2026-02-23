#Automate Web Browser Scraping using Selenium

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
  print("Launching chrome browser ...")
  
  #Tell where the chrome driver is
  #Link : https://googlechromelabs.github.io/chrome-for-testing/#stable
  chrome_driver_path = "./chromedriver"
  #How the chrome web driver should operate like headless mode or ignore images
  options = webdriver.ChromeOptions()
  #Setup Driver to get data and html
  driver = webdriver.Chrome(service = Service(chrome_driver_path),options = options)

  try:
    #Grab the content from the website
    driver.get(website)
    print("Page loaded ...")
    html = driver.page_source
    time.sleep(10)

    return html
  finally:
    driver.quit()
