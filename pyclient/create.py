import requests

endpoint = 'http://localhost:8000/api/products/'   # here is the website you want to access

#json 
data = {
    "title" : "This is a new product",
}
get_response = requests.post(endpoint , json= data) # get the response in form of html
print (get_response.json())
