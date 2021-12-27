import requests
import pandas
import GoogleSearch
from googlesearch import GoogleSearch
gs = GoogleSearch("An intriguing query")
for url in gs.top_urls():
  print(url)







