import requests

TOKEN = None

url = "https://notify-api.line.me/api/notify" 
token = TOKEN
headers = {"Authorization" : "Bearer "+ token} 
message =  "@All あけおめ！！！！" 
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload)