import requests



headers = {'Authorization': 'Token 9f841e8a2b6c7fb10278f6af8321425edc2ff238'}  # here is the token you get from the login if it change it will not run 
endpoint = 'http://localhost:8000/api/products/'   # here is the website you want to access

#json 
data = {
    "title" : "This is a new product",
}
get_response = requests.post(endpoint , json= data , headers = headers) # get the response in form of html
print (get_response.json())
