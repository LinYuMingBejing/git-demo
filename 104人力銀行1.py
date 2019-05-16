import requests
from bs4 import BeautifulSoup as bs
import re
import csv
headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"}
base_url=[]
for page in range(20):
    url=("https://m.104.com.tw/search/joblist?m=2&ro=0&kwop=7&keyword=python&order=1&asc=0&page=2&mode=s&jobsource=2018indexpoc&page=%s"%page)
    base_url.append(url)
for info_url in base_url:
    res=requests.get(info_url,headers=headers)
    
    soup=bs(res.text,"lxml")
    job_tags=soup.select("li",class_="items")
    content0=[]
    content1=[]
    content2=[]
    content3=[]
    content4=[]
    content5=[]
    content6=[]
    content7=[]
    content8=[]
    for job_tag in job_tags:
        # 工作名稱
        job_names=job_tag.select("h2",class_="title")
        for job_name in job_names:
            job_name=job_name.get_text()
            
            # content={"工作名稱":job_name}
            content0.append(job_name)

        company_names=job_tag.select("h3",class_="company")
           
        #公司名稱
        for company_name in company_names:
            company_name=company_name.get_text()
            
            content1.append(company_name)
        
        tags=job_tag.select("p")
        for index,tag in enumerate(tags):
            
            if index==0:
                all_info=tag.get_text()    
                
                all_info=all_info.replace(" | ",",")           
                all_info=all_info.split(",")
                #公司地址
                address=all_info[0]
                requirement=all_info[1]
                graduate=all_info[-1]
                
                content2.append(address)
                content3.append(requirement)
                content4.append(graduate)
            if index==1:
                all_info=tag.get_text()
                skill=all_info.replace("\r\n","")
                
                content5.append(skill)


        wage_tags=job_tag.select("a > div",class_="tag")
    
        for index,wage_tag in enumerate(wage_tags):
            if index==0:
                wage=wage_tag.get_text()
                
                content6.append(wage)
            if index==1:
                company_scale=wage_tag.get_text()
                
                content7.append(company_scale)
        
    with open ("python工作表2.csv","w",encoding="utf-8-sig",newline="") as file:
        writer = csv.writer(file)
        
        writer.writerows(zip(content0,content1,content2,content3,content4,content5,content6,content7))


