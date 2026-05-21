import requests

r = requests.post('https://httpbin.org/post', data={'mradul': 'value'})
print(r.text)