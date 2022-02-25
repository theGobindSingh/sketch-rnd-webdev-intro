# import os
# import requests #pip install requests
# import json

# folder_name="vogue"     #This folder will be created in Documents

# docs = os.path.expanduser("~/Documents").replace("\\","/") + "/"

# try:
#     os.mkdir(docs+folder_name)
# except:
#     print("")

# loc = docs+folder_name
# print ("save location: "+loc)

# for x in range(0,16):
#     url_main="https://api.vogue.it/production/photos?count=16&date_from=2021-04-01&date_to=2021-04-16&isDaily=true&locale=en-us&page=0&type_ids=3"
#     m=requests.get(url_main)
#     mjs=json.loads(m.text)
#     img_name=(mjs["items"][x]["title"]).replace('"',"")
#     img_link=str(mjs["items"][x]["gallery_image"])

#     with open(os.path.join(loc,img_name+".png"),"wb") as f:
#         f.write(requests.get(img_link).content) 
#     f.close()

import os
import requests #pip install requests
import json
from bs4 import BeautifulSoup

folder_name = "galaxy_photos"

docs = os.path.expanduser("~/Documents").replace("\\","/") + "/"

try:
    os.mkdir(docs+folder_name)
except:
    print("")

loc = docs+folder_name
print ("save location: "+loc)
req = requests.get("https://nasasearch.nasa.gov/search/images?affiliate=nasa&query=galaxy").text
obj = BeautifulSoup(  req  ,"lxml")
obj.find("results-wrapper")

print(obj)
