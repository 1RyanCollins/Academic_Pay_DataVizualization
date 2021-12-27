import requests
import pandas
from googlesearch import GoogleSearch
gs = GoogleSearch("An intriguing query")
for url in gs.top_urls():
  print(url)







