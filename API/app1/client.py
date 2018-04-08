import requests
#resp=requests.get("http://localhost:8000/custs/")
#requests.post, To create customer
#requests.put: to modify the customer
#requests.get: to get the list of customers
#resquest.delete: to delete customer 
'''
resp = requests.post("http://localhost:8000/customer/",json={"name":"cust1",
	"email":"email1@gmail.com","phone":"9676622023"})
print resp.json()
resp=requests.get("http://localhost:8000/customer/2/",
	headers={'Content-Type': 'application/json'})
print resp.json()
resp=requests.delete("http://localhost:8000/customer/2/",
	headers={'Content-Type': 'application/json'})
print resp.json()
'''
resp = requests.put("http://localhost:8000/customer/3",
	data={"name":"cust3_modifield"})
print resp.json()