import streamlit as st
import pandas as pd
import LighthouseRunner
  

st.write("SEO Project - Google Lighthouse Automation")

report = LighthouseRunner('https://www.espn.com/', form_factor='desktop', quiet=False).report
print(report)
