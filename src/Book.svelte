<script>
    export let name;
    export let age;
    let clicks=0;
    function funClick(){
        clicks+=1;
    }
</script>

<main>
    <p>Hello {name}, you are {age} years old.</p>
    <button on:click={funClick}>Clicked {clicks} {clicks===1 ? 'time' : 'times'}</button>
</main>