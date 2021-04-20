import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "f99790104227f53cf2120efd4ac1cdaa",
    "redirect_uri" : "https://localhost.com",
    "code"         : "BACawlPo8No-_YQP8ZMyk-zWQdDjrlMbNkdJwMFOvvD0BQ6o1-x5rnRyH2VilRRHINvIcwopyV4AAAF21jkW9Q"
                      
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)