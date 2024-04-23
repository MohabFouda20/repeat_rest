const loginForm = document.getElementById('LoginForm');
const searchForm = document.getElementById('SearchForm');
const ContentContainer = document.getElementById('content-container');
const baseEndpoint = 'http://localhost:8000/api';
if (loginForm){
loginForm.addEventListener('submit', handleLogin)
}
if (searchForm){
    loginForm.addEventListener('submit', handlesearch)
    }
    

function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData) // we fget the user name and password from the form 
    let bodyjson= JSON.stringify(loginObjectData) // convert it into a json string to handle it with the api 
    console.log(loginObjectData)
    const option =getFetchOption('POST', bodyjson)
    fetch(loginEndpoint, option) // request.post 
    .then(response =>response.json())
    .then(authData => handleAuthData(authData ,getProductList))
    .catch(error => console.log(error))
}

function handlesearch(event){
    console.log(event)
    event.preventDefault()
    let FormData = new FormData(searchForm)
    let Data = Object.fromEntries(FormData) // we fget the user name and password from the form 
    let searchParams = new URLSearchParams(Data)

    const Endpoint = `${baseEndpoint}/search/?${searchParams}`


    const option ={
        method : 'GET',
        headers : {
            'Content-Type': 'application/json',
    }}


    fetch(Endpoint, option) // request.get 
    .then(response =>response.json())
    .then(data => 
    { 
        console.log(data.hits)
        writeToContainer(data)
    }
    )
    .catch(error => console.log(error))
}





function isTokenExpired(jsonData){
    if (jsonData.code && jsonData.code === 'token_not_valid'){
        alert('Token is expired , please login again') 
        return false;
    }
    return true;
}


function handleAuthData(authData , callback){
    localStorage.setItem('access' , authData.access)
    localStorage.setItem('refresh' , authData.refresh) 
    if (callback){
        callback()
    }

}



function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const option =getFetchOption()
    fetch(endpoint, option)
    .then(response => response.json()).then(data=>
        {   isTokenExpired(data)
            console.log(data)
        writeToContainer(data)
    }
    ).catch(error => console.log(error))
}


function writeToContainer(data) {
    if (ContentContainer) {
        ContentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOption(method, body){
    return {
        method : method === null ? "GET" : method ,
        headers : {
            'Content-Type': 'application/json',
            'authorization': 'Bearer ' + localStorage.getItem('access') // or we can use string substitution `Bearer ${localStorage.getItem('access')}`
        },
        body : body ? body : null
    }}

function ValidToken (){
    const endpoint = `${baseEndpoint}/token/verify/`
    body = JSON.stringify({token : localStorage.getItem('access')})
    const option = getFetchOption('POST' , body)
    fetch(endpoint, option)
    .then (response => response.json())
}