<script>
    function funShowTrade(){
        return alert('hello trade');
    }
    function funShowDiscover(){
        return alert('hello trade');
    }
    function funShowCharts(){
        return alert('hello trade');
    }
    function funShowPositions(){
        return alert('hello trade');
    }
    function funShowOrders(){
        return alert('hello trade');
    }
    function funShowHistory(){
        return alert('hello trade');
    }
    function func(){
        console.log('test');
    }

</script>

<main>
    <div class="btn-group">
        <button on:click={funShowTrade}>
            1
        </button>
        <button on:click={funShowDiscover}>
            2
        </button>
        <button on:click={funShowCharts}>
            3
        </button>
        <button on:click={funShowPositions}>
            4
        </button>
        <button on:click={funShowOrders}>
            5
        </button>
        <button on:click={funShowHistory}>
            6
        </button>
        <button on:click={func}>Login</button>
      </div>
</main>

<style>
.btn-group button {
  background-color: #4CAF50; /* Green background */
  border: 1px solid green; /* Green border */
  color: white; /* White text */
  padding: 10px 24px; /* Some padding */
  cursor: pointer; /* Pointer/hand icon */
  width: 50%; /* Set a width if needed */
  display: block; /* Make the buttons appear below each other */
}

.btn-group button:not(:last-child) {
  border-bottom: none; /* Prevent double borders */
}

/* Add a background color on hover */
.btn-group button:hover {
  background-color: #3e8e41;
}
</style>