import streamlit as st
import pandas as pd
import requests
import json
import csv
from time import sleep

API_Key = "AIzaSyDRuzgTAl1eFBKd5bpZ8MAqdIW-ThxYTG8"

import pagespeed
ps = pagespeed.PageSpeed()
response = ps.analyse('https://www.espn.com', strategy='desktop')
print(response.speed)
  

st.write("SEO Project - Google Lighthouse Automation")

report = LighthouseRunner('https://www.espn.com/', form_factor='desktop', quiet=False).report
print(report)
