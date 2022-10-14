
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# PD!
table = {
    "rating":[],
    "name(ja)":[],
    "name(en)":[],
    
}

page = 59
while True:
    print("頁數:", page)
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    try:
        response = urlopen(url)
    except HTTPError:
        print("最後一頁了吧!")
        # PD! DataFrame: pandas表格
        df = pd.DataFrame(table)
        df.to_csv("tabelog.csv", encoding="utf-8", index=False)
        break
    page = page + 1
    html = BeautifulSoup(response)

    # a = html.find("a", {"class":"list-rst__name-main"})
    # 如果你用這寫法, class_加下底線
    lis = html.find_all("li", class_="list-rst")
    for li in lis:
        en = li.find("a", class_="list-rst__name-main")
        ja = li.find("small", class_="list-rst__name-ja")
        rating = li.find("b", class_="c-rating__val")
        prices = li.find_all("span", class_="c-rating__val")
        print(rating.text, ja.text, en.text)
        print(en["href"])
        print("晚間價錢:", prices[0].text)
        print("午間價錢:", prices[1].text)
        print("-" * 30)
        # PD!
        table["rating"].append(rating.text)
        table["name(ja)"].append(ja.text)
        table["name(en)"].append(en.text)