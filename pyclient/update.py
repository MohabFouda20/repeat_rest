import requests


pppk  = int (input("Enter the product id you want to update : "))
if pppk :
    
    endpoint = f'http://localhost:8000/api/products/{pppk}/update/'   # here is the website you want to access


    data= {
        "title": "this is after update" , 
        "price" : 500
    }
    #json 

    get_response = requests.put(endpoint , json=data) # get the response in form of html
    print (get_response.status_code)
