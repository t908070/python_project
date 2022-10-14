import os
import json
from urllib.request import urlopen , urlretrieve
if not os.path.exists("google"):
    os.makedirs("google")
for i in range(6) :

    print("月份" , i + 1)
    url = "https://www.google.com/doodles/json/2022/"+ str(i + 1) + "?hl=zh_TW"

    response =  urlopen(url)
    plist = json.load(response)
    for pdic in plist:
        print(pdic["title"])
        img = ("https:" + pdic["url"])
        fn = "google/" + img.split("/")[-1]
        urlretrieve(img , fn)
        print(img.split("/"))