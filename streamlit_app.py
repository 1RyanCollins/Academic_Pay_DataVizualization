import requests
import pandas
import streamlit as st
from bs4 import BeautifulSoup

 
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
st.title(SEO Keyword Web App)
st.text(soup.prettify())










