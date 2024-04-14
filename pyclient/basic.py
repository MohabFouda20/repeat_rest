import requests


# endpoint = 'http://httpbin.org/anything/'   # here is the website you want to access
endpoint = 'http://localhost:8000/api/'   # here is the website you want to access

#json 

get_response = requests.post(endpoint ,json={"title":"hello worldd"}) # get the response in form of html
# print (get_response.text)
print (get_response.json())
print (get_response.status_code)