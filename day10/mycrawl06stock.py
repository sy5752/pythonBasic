# import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  
bsObject = BeautifulSoup(html, "html.parser") 


td = bsObject.select('.st2')


for i in td :
    s_code = i.find(["a"]).get("title")
    s_name = i.text
    s_price = i.parent.select("td")[1].text
    print("s_code : " , s_code, end=" ")
    print("s_name : " , s_name, end=" ")
    print("s_price : " , s_price)


