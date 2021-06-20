export default class Test{
    data=[]
    data1=[]
    constructor(){
        
        for(var i = 0; i<7; i++)
        {
            var a = {value: Math.floor(Math.random() * 15000).toString()};
            this.data.push(a);
        }
        console.log(this.data);
        fetch('https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-09?apiKey=OriEh_f_1zZncSE0CZsMqsizk0EY4ael')
        .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
        .then(damn => damn['results'].forEach(element => this.data1.push(
            new Object(
            {
                value: Math.floor(element.o).toString()
            })
            )
        ));
        console.log(this.data1);
        console.log("Size of 2nd array is "+this.data1.length.toString())
    }
}