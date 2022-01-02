import requests
import pandas
import streamlit as st
from bs4 import BeautifulSoup
from googlesearch import search


#run a google search 
#keyword

#top10 results
results = search("Google", num_results=10)


#url
url = "https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
st.title("SEO Keyword Web App")
st.text(results)











