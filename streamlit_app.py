import streamlit as st
import pandas as pd
import requests
import json
import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

 
st.write("SEO Project - Google Lighthouse Automation")
st.write(soup.prettify())


