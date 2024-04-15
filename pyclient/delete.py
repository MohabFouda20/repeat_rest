import requests

product_id = int (input("Enter the product id you want to delete: "))

if product_id :
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete'   # here is the website you want to access
    
    get_response = requests.delete(endpoint) # get the response in form of html
    print (get_response.status_code)
