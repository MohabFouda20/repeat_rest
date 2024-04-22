import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'   

password = getpass('Password: ')


auth_response = requests.post(auth_endpoint , json= {'username': 'fouda', 'password': password}) # get the response in form of html


print (auth_response.json())


if auth_response.status_code == 200 :
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Token {token}'
    }
    endpoint = 'http://localhost:8000/api/products/'   # here is the website you want to access

    #json 


    get_response = requests.get(endpoint , headers= headers ) # get the response in form of html
    print (get_response.json())


