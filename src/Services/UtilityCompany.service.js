const REGISTER_UTILITY_URL = 'http://127.0.0.1:5001/register_utility';
const GET_UTILITY_URL = 'http://127.0.0.1:5001/get_utility';

export function register_utility(){
    var name = document.getElementById("utilityName").value;
    var coinsBalance = document.getElementById("ucoinsBalance").value;
    var energyValue= document.getElementById("uenergyValue").value;
    var energyUnits= document.getElementById("uenergyUnits").value;

    var json = {
        'name': name,
        'coinsBalance' : coinsBalance,
        'energyValue' : energyValue,
        'energyUnits' : energyUnits
    }
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", REGISTER_UTILITY_URL);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
    }};

    xhr.send(JSON.stringify(json));

}


export function get_utility(){
    fetch(GET_UTILITY_URL)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
    })
}