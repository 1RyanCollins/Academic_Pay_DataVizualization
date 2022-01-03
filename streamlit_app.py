import requests
import pandas
import streamlit as st
from bs4 import BeautifulSoup
from googlesearch import search

#url_input = st.text_input("Enter your keyword")

#run a google search 
#keyword

#top10 results
#results = []

#####code here to pull search results#######


#for item in results: 
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title

    
###determine position in results####

st.title("SEO Keyword Web App")

st.text(title)
print(title)















