import streamlit as st
import pandas as pd
pip install https://github.com/adamcupial/lighthouse-python
from lighthouse import LighthouseRunner
  

st.write("SEO Project - Google Lighthouse Automation")

report = LighthouseRunner('https://www.espn.com/', form_factor='desktop', quiet=False).report
print(report)
