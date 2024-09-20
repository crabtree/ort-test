import requests

response = requests.get("https://api.ipify.org?format=json").json()
print(response)