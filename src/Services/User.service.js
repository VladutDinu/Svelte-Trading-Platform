    const REGISTER_URL = 'http://127.0.0.1:5001/register_user';
    const GET_USERS_URL = 'http://127.0.0.1:5001/get_users';
    const LOGIN_URL = 'http://127.0.0.1:5001/login_user';
    export function register_user(){
        var username = document.getElementById("username").value;
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        var json = {
            'username': username,
            'email' : email,
            'password' : password
        }
        
        var xhr = new XMLHttpRequest();
        xhr.open("POST", REGISTER_URL);

        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }};

        xhr.send(JSON.stringify(json));

    }

    export function get_users(){
        fetch(GET_USERS_URL)
        .then(response => response.json())  
        .then(json => {
            console.log(json);
        })
    }
    
    export function login_user(){
        var username = document.getElementById("username").value;
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        var json = {
            'username': username,
            'email' : email,
            'password' : password
        }
        var xhr = new XMLHttpRequest();
        xhr.open("GET", LOGIN_URL+'?email='+email);

        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }};

        xhr.send(JSON.stringify(json));
   
    }