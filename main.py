#Create a Basic Streamlit UI
import streamlit as st

#Using Selenium Scraper inside Streamlit
from scrape import scrape_website

st.title("AI Web Scraper")

url = st.text_input("Enter a Website URL : ")

if st.button("Scrape Site"):
  st.write("Scraping the website")
  result = scrape_website(url)
  print(result)