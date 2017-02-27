import requests

#resp = requests.get("http://localhost:8888/employeesjson")
#print resp, resp.json()

resp = requests.get("http://localhost:8888/employees/salaryavg")
print resp, resp.json()