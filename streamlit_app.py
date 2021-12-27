import requests
import pandas
import urlparse4
import requests_html
from requests_html import HTMLSession

try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)
    
title =  response.html.find('title')
title = title[0].text



st.write("SEO Project - Google Lighthouse Automation")
st.write(title)


