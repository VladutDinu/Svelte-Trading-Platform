const REGISTER_BANK_URL = 'http://127.0.0.1:5001/register_bank';
const GET_BANKS_URL = 'http://127.0.0.1:5001/get_banks';

export function register_bank(){
    var name = document.getElementById("bankName").value;
    var coinsBalance = document.getElementById("coinsBalance").value;
    var cashBalance = document.getElementById("cashBalance").value;
    var cashCurrency = document.getElementById("cashCurrency").value;

    var json = {
        'name': name,
        'coinsBalance' : coinsBalance,
        'cashBalance' : cashBalance,
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


export function get_banks(){
    fetch(GET_BANKS_URL)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
    })
}