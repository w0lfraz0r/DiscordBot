from bs4 import BeautifulSoup
from bs4.element import Comment
# import pandas as pd
# import numpy as np
import requests
# ['data']['Catalog']['searchStore']['elements']['0']['title']
#['data']['Catalog']['searchStore']['elements']['0']['description']
# ['data']['Catalog']['searchStore']['elements']['0']['effectiveDate']
# ['data']['Catalog']['searchStore']['elements']['0']['keyImages']


url='https://www.epicgames.com/store/en-US/free-games'
urlb='https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=IN&allowCountries=IN'

xml_data = requests.get(urlb).content
print(xml_data)
goodData=dict(xml_data)
print("\n\n\n")
print("ho hi ha ho")
print(goodData)
soup = BeautifulSoup(xml_data, "lxml")
 
# Find all text in the data
# texts = str(soup.findAll(text=True)).replace('\\n','')
    
#Find the tag/child
child = soup.find("elements")
    
Title = []
Description = []
EffectiveDate = []
KeyImagesurl = []
EndDate = []

    
while True:    
    try:
        Description.append(" ".join(child.find('description')))
    except:
        Description.append(" ")
            
    try:
        Title.append(" ".join(child.find('title')))
    except:
        Title.append(" ")
        
    try:
        EffectiveDate.append(" ".join(child.find('effectiveDate')))
    except:
        EffectiveDate.append(" ")
            
    try:
        EndDate.append(" ".join(child.find('endDate')))
    except:
        EndDate.append(" ")
        
    try:   
        # Next sibling of child, here: entry 
        child = child.find_next_sibling('entry')
    except:
        break
    
data = []
# data = pd.DataFrame({"updated":updated,
#                                     "Title":Title,
#                                     "EffectiveDate":EffectiveDate,
#                                     "rating":rating,
#                                     "user_name":user_name})
# final_data = final_data.append(data, ignore_index = True)
print("Title",Title)
print("Description",Description)
print("EffectiveDate",EffectiveDate)
print("KeyImagesurl",KeyImagesurl)
print("EndDate",EndDate)

