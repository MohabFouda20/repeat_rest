import requests

endpoint = 'http://localhost:8000/api/products/2/'   # here is the website you want to access

#json 

get_response = requests.get(endpoint) # get the response in form of html
print (get_response.json())
