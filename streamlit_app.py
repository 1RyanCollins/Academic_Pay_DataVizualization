import streamlit as st
import pandas as pd
import requests
import json
import csv
from time import sleep

API_Key = "AIzaSyDRuzgTAl1eFBKd5bpZ8MAqdIW-ThxYTG8"
url = 'https://www.espn.com/'


import urllib.request, json

#Note that you can insert your URL with the parameter URL and you can also modify the device parameter if you would like to get the data for desktop.
response = urllib.request.urlopen(url, key=API+Key)
data = json.loads(response.read())  

overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100


 
st.write("SEO Project - Google Lighthouse Automation")
st.write(overall_score)


