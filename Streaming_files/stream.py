import requests

url="https://www.win-rar.com"
r=requests.get(url,stream=True)
totalExpectedBytes=int(r.headers['Content-Length'])
bytesRecived=0
with open('Streaming_files/winrar.wav','wb')as f:
    for chunk in r.iter_content(chunk_size=128):
        print(f"{bytesRecived} recived out of total {totalExpectedBytes}")
        f.write(chunk)
        bytesRecived+=128