#Automate Web Browser Scraping using Selenium
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

#Using BeautifulSoup for parsing the data
from bs4 import BeautifulSoup

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

    return html
  finally:
    driver.quit()

#Remove unnecessary DOM content
def extract_body_content(html_content):
  soup = BeautifulSoup(html_content,"html.parser")
  body_content = soup.body
  if body_content:
    return str(body_content)
  return ""

#Clean the content to be passed to LLM
def clean_body_content(body_content):
  soup = BeautifulSoup(body_content,"html.parser")

  for script_or_style in soup(["script","style"]):
    script_or_style.extract()
    
  cleaned_content = soup.get_text(separator = "\n")
  cleaned_content = "\n".join(
    #Remove additional \n characters
    line.strip() for line in cleaned_content.splitlines() if line.strip()
  )

  return cleaned_content

#Since LLM can only handle 6000 chars at once, split into batches
def split_dom_content(dom_content,max_length = 6000):
  return[
    dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
  ]