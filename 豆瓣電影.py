import requests
from bs4 import BeautifulSoup as bs
import csv
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
import re
x0=[0,1,2,3,4,5,6,7,8,9]
numbers=[]
for x in x0:
    y=25*x
    numbers.append(y)
contents=[]
for number in numbers:
    
    res=requests.get("https://movie.douban.com/top250?start=%s&filter="%(number),headers=headers)

    soup=bs(res.text,"lxml")

    title_tag=soup.select("ol",calss_="grid_view")[0]
    titles=title_tag.select("li")
    for title in titles:
        Chinese_name=title.select("span",class_="title")[0].get_text()
        Eng_name=title.select("span",class_="title")[1].get_text()
        
        
        Eng_name=Eng_name.replace(" / ","")
        Eng_name=Eng_name.replace("\xa0/\xa0","")
        other_name=title.select("span",class_="title")[2].get_text()
        other_name=other_name.replace('\xa0/\xa0','')
        actor=title.select("p")[0].get_text()
             
        actor=actor.strip()
        actor=actor.replace("\n","")
        actor=actor.replace("  ","")
        
        actor=actor.replace("..."," , ")
        actor=actor.replace("/",",")
        
        actor=re.sub("主演:","/s主演:",actor)
        actor=re.sub("/s",", ",actor)
        actor=actor.replace("\xa0","")
        actor=actor.strip()
        actor=actor.split(",")
        director=actor[0]
        actress=actor[1]
        founded=actor[-3]
        
        country=actor[-2]      

        
        rating=title.select("div",class_="bd")[0]
        
        rating=rating.select("div",class_="star")[-1].get_text()
        rating=rating.strip()
        #有2個 \n 符號
        rating=rating.replace("\n",'',1)
        rating=rating.replace("\n",',') 
        rating=rating.replace("评价",'')
        rating=rating.split(",")
        movie_rating=rating[0]
        movie_views=rating[1]
        
        
        content={"電影名稱":Chinese_name,
        "英文名稱":Eng_name,
        "其他名稱":other_name,
        "導演":director,
        "演員":actress,
        "年份":founded,
        "出產國家":country,
        "星等":movie_rating,
        "觀看人數":movie_views
        }
        contents.append(content)

headers=["電影名稱","英文名稱","其他名稱","導演","演員","年份","出產國家","星等","觀看人數"]
with open("豆瓣電影列表0.csv","w",encoding="utf-8-sig",newline="") as file:

    writer=csv.DictWriter(file,headers)
    writer.writeheader()
    writer.writerows(contents)

    

