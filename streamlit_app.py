import requests
import pandas
import streamlit as st
from bs4 import BeautifulSoup
from googlesearch import search

url_input = st.text_input("Enter your keyword")

#run a google search 
#keyword

#top10 results
results = []
for j in search(url_input, tld="co.in", num=10, stop=10, pause=2):
    results.append(j)

#url
url = "https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
st.title("SEO Keyword Web App")
st.text(results)











