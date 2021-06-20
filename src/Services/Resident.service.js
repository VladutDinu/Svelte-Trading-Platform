const REGISTER_RESIDENT_URL = 'http://127.0.0.1:5001/register_resident';
const GET_RESIDENT_URL = 'http://127.0.0.1:5001/get_residents';

export function register_resident(){
    var firstName = document.getElementById("rfirstName").value;
    var lastName = document.getElementById("rlastName").value;
    var coinsBalance = document.getElementById("rcoinsBalance").value;
    var cashBalance  = document.getElementById("rcashBalance").value;
    var energyValue = document.getElementById("renergyValue").value;
    var energyUnits = document.getElementById("renergyUnits").value;
    var cashCurrency = document.getElementById("rcashCurrency").value;

    var json = {
        'firstName': firstName,
        'lastName': lastName,
        'coinsBalance' : coinsBalance,
        'cashBalance' : cashBalance,
        'energyValue' : energyValue,
        'energyUnits' : energyUnits,
        'cashCurrency' : cashCurrency
    }
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", REGISTER_BANK_URL);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
    }};

    xhr.send(JSON.stringify(json));

}


export function get_resident(){
    fetch(GET_RESIDENT_URL)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
    })
}