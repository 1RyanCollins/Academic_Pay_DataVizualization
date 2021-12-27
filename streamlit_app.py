import requests
import pandas

from googlesearch import search
query = "Geeksforgeeks"
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(st.write(j))







