import requests
import pandas


try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)
    
title =  response.html.find('title')
title = title[0].text



st.write("SEO Project - Google Lighthouse Automation")
st.write(title)


