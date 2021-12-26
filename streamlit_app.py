import streamlit as st
import pandas as pd
import requests
import json
import csv
from time import sleep

API_Key = "AIzaSyDRuzgTAl1eFBKd5bpZ8MAqdIW-ThxYTG8"
base_URL = 'https://www.espn.com/'
  
def get_pagespeed(API_Key, page_URL, baseURL, strategy):
    response_url = baseURL+page_URL+'&key='+API_Key+'&strategy='+strategy
    response = requests.get(response_url)
    json_data = response.json()
    lighthouseResult = json_data["lighthouseResult"]
    categories = lighthouseResult["categories"]
    performance = categories["performance"]
    score = performance["score"]
    return (score*100)
    sleep(1)
    
 
st.write("SEO Project - Google Lighthouse Automation")

get_pagespeed()
