#import libraries
import streamlit as st
import pandas as pd
import json
import csv
from time import sleep
import requests
pip install bs4
from bs4 import BeautifulSoup

#get pagee
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")

#print response code
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

#get title
Title = soup.title
 
st.write("SEO Project - Google Lighthouse Automation")
st.write(Title)


