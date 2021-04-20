from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://192.168.42.31:8081/HELLOWEB2/mycrawl")  
bsObject = BeautifulSoup(html, "html.parser") 

print(bsObject)

td = bsObject.select('td')

for i in td :
    print(i.text)
