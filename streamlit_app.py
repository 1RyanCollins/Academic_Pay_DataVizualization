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
r = requests.get('https://en.wikipedia.org/wiki/List_of_dog_breeds')
soup = BeautifulSoup(r.content, features="lxml")
title = soup.find("title")

    
###determine position in results####

st.title("SEO Keyword Web App")

st.text(title)
print(title)















