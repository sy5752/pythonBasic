from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import datetime

conn = pymysql.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'java', 
    db = 'python', 
    charset = 'utf8'
)
curs  = conn.cursor()

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  
bsObject = BeautifulSoup(html, "html.parser") 


td = bsObject.select('.st2')

now = datetime.datetime.now()
in_time = now.strftime("%Y%m%d,%H%M")

for i in td :
    s_code = i.find(["a"]).get("title")
    s_name = i.text
    s_price = i.parent.select("td")[1].text.replace(",","")
    print("s_code : " , s_code, end=" ")
    print("s_name : " , s_name, end=" ")
    print("s_price : " , s_price)
    sql = "select s_price from stock where s_code<=001065"
    cnt = curs.execute(sql)
    
conn.commit()
conn.close()
  
    





