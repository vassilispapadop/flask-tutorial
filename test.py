import requests

baseurl = 'http://127.0.0.1:5000/'

response = requests.get(baseurl + 'api/video', params={'key':2})
data = response.content
print(data)