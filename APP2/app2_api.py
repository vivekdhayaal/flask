import requests
resp = requests.post("http://localhost:8888/createemp", json = {'empname':'harini1','password':'xxxx', 'address':'ad1'})
print resp.status_code

