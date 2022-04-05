#!/usr/bin/env python
# coding: utf-8

# In[103]:


import json
import requests
import pandas as pd

url = "https://www.myopia.care/callers/storelocator.php"

r = requests.get(url)

rj = json.loads(r.text)

rjnest = rj["features"]

businesslist=[]

for x in rjnest:
    name = x["company-name"]
    address1 = x["company-address"]
    address2 = x["company-address2"]
    postcode = x["company-zip"]
    city = x["company-city"]
    country = x["countrycode"]
    openinghours = x["business_hours"]
    email = x["email"]
    tel = x["tel"]
    mobile = x["mobile"]
    website = x["website"]
    coordx = x["Xcoord"]
    coordy = x["Ycoord"]
    
    business = {
        "CompanyName": name,
        "Address 1": address1,
        "Address 2": address2,
        "Postcode": postcode,
        "City": city,
        "Country": country,
        "OpeningHours": openinghours,
        "Email": email,
        "Tel": tel,
        "Mobile": mobile,
        "Website" : website,
        "CoordinateX": coordx,
        "CoordinateY": coordy,
    }
    businesslist.append(business)


df = pd.DataFrame.from_dict(businesslist)
df.head()

df.to_csv('MyopiaCareSpecialists.csv', encoding='utf-8-sig')


# In[ ]:




