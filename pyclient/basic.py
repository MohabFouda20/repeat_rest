import requests


endpoint = 'http://localhost:8000'   # here is the website you want to access

#json 

get_response = requests.get(endpoint , json = {"query" : "hello world"}) # get the response in form of html
print (get_response.text)
print (get_response.json())