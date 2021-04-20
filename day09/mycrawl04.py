import requests
import json

url = "https://dapi.kakao.com/v2/search/cafe"
queryString = {"query":"대전맛집"}
header = {'authorization':'KakaoAK dfb7c43baee03e8df2000f19256be953'}
r = requests.get(url, headers=header, params=queryString)

jsonObj = json.loads(r.text)
docus = jsonObj.get("documents")

for i in docus :
    print("cafename:", i.get("cafename") ,end=",")
    print("contents:", i.get("contents") ,end=",")
    print("datetime:", i.get("datetime") ,end=",")

    print("thumbnail:", i.get("thumbnail") ,end=",")
    print("title:", i.get("title") ,end=",")
    print("url:", i.get("url"))
    
 

