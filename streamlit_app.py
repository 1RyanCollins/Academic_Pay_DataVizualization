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
page = requests.get("https://en.wikipedia.org/wiki/List_of_dog_breeds")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title 
title = title.contents

#word_list = title.split()
#number_of_words = len(word_list)
#position = word_list.index("one")+1

#
    

st.title("SEO Keyword Web App")
st.text(type(title))
















