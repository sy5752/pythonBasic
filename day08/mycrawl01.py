from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.42.31:8081/HELLOWEB2/crawl.jsp")  

print(html)

bsObject = BeautifulSoup(html, "html.parser") 

td = bsObject.select("td")
#  td = bsObject.find_all('td')

for i in td : 
    print(i)