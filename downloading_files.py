import requests
url="https://www.win-rar.com"

r=requests.get(url)
fp=open("winrar.exe","wb")
fp.write(r.content)
fp.close()