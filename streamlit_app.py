import streamlit as st
import pandas as pd
import requests
import json
import csv
from time import sleep

  
import requests
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)


 
st.write("SEO Project - Google Lighthouse Automation")
st.write(r.content)


