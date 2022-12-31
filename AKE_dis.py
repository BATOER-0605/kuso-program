import requests

TOKEN = 'w9QAStKokL5bdARF7gEWoOrRWJ55W4R9R8GT0o5BuN2'

url = "https://notify-api.line.me/api/notify" 
token = TOKEN
headers = {"Authorization" : "Bearer "+ token} 
message =  "@All あけおめ！！！！" 
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload)