import requests
import pandas
import streamlit as st
from bs4 import BeautifulSoup

# scraping a wikipedia article
url_link = 'https://www.geeksforgeeks.org/how-to-scrape-all-pdf-files-in-a-website/'
request = requests.get(url_link)
 
Soup = BeautifulSoup(request.text, 'lxml')
 
# creating a list of all common heading tags
heading_tags = ["h1", "h2", "h3"]
for tags in Soup.find_all(heading_tags):
    st.text((tags.name + ' -> ' + tags.text.strip()))
    










