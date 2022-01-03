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
html = "https://www.bbc.com/culture/article/20210902-the-power-of-the-dog-a-five-star-brooding-melodrama"
soup = BeautifulSoup(html, 'html.parser')
title = soup.find("title")

    
###determine position in results####

st.title("SEO Keyword Web App")
st.text(title)

for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.name + ' ' + heading.text.strip())













