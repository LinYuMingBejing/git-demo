import requests
from bs4 import BeautifulSoup as bs
import csv
headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"}


s = requests.Session()
urls=["https://movies.yahoo.com.tw/chart.html","https://movies.yahoo.com.tw/chart.html?cate=rating"]
contents=[]
for url in urls:
    res=s.get(url,headers=headers)
    soup=bs(res.text,"lxml")
    movie_tags=soup.select("main > ul > li")
    
    

    for movie_tag in movie_tags:
            
        movie_name=movie_tag.select("h2")[0].get_text()
        english_name=movie_tag.select("h3")[0].get_text()
        movie_date=movie_tag.select("span")[-2].get_text()
        star=movie_tag.select("span")[-1].get_text()
        reaction=movie_tag.select("h3")[-1].get_text()
        
        content2={"電影名稱":movie_name,
                "英文名稱":english_name,
                "上映日期":movie_date,
                "推薦指數":star,
                "影迷評論":reaction}
        contents.append(content2)


headers=["電影名稱","英文名稱","上映日期","推薦指數","影迷評論"]
with open ("台北電影排行.csv","w",encoding="utf-8-sig",newline="")as fp:
    writer=csv.DictWriter(fp,headers)
    writer.writerows(contents)
    