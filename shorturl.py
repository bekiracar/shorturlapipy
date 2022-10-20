import requests
url = input("Lütfen kısaltmak istediğiniz linki giriniz:")
response = requests.get("https://short-link-api.vercel.app/?query="+url)
print(response.json()['da.gd'])

