<script>
    import {register_bank, get_banks} from "./Services/Bank.service.js";
    import {register_resident, get_resident } from "./Services/Resident.service.js";
    import {register_utility, get_utility} from "./Services/UtilityCompany.service.js";
    import {register_user, get_users, login_user} from "./Services/User.service.js";
    

</script>

<main>
    <div class="login">
        <input id= username type="text" name="username" placeholder="Username"/>
        <input id= email type="text" name="email" placeholder="Email"/>
        <input id= password type="password" name="password" placeholder="password"/>
        <button on:click={register_user}>Register</button>
        <button on:click={login_user}>Login</button>
        <button on:click={get_users}>Get Users</button>
    </div>

    <div class="utility">
        <input id= utilityName type="text" name="utilityName" placeholder="utilityName"/>
        <input id= ucoinsBalance type="text" name="ucoinsBalance" placeholder="coinsBalance"/>
        <input id= uenergyValue type="text" name="uenergyValue" placeholder="energyValue"/>
        <input id= uenergyUnits type="text" name="uenergyUnits" placeholder="energyUnits"/>
        <button on:click={register_utility}>Register</button>
        <button on:click={get_utility}>Get Utilities</button>
    </div> 
    <div class="bank">
        <input id= bankName type="text" name="bankName" placeholder="bankName"/>
        <input id= coinsBalance type="text" name="coinsBalance" placeholder="coinsBalance"/>
        <input id= cashBalance type="text" name="cashBalance" placeholder="cashBalance"/>
        <input id= cashCurrency type="text" name="cashCurrency" placeholder="cashCurrency"/>
        <button on:click={register_bank}>Register</button>
        <button on:click={get_banks}>Get Banks</button>
    </div>
    <div class="resident">
        <input id= rfirstName type="text" name="rfirstName" placeholder="firstName"/>
        <input id= rlastName type="text" name="rlastName" placeholder="lastName"/>
        <input id= rcoinsBalance type="text" name="rcoinsBalance" placeholder="coinsBalance"/>
        <input id= renergyValue type="text" name="renergyValue" placeholder="energyValue"/>
        <input id= renergyUnits type="text" name="renergyUnits" placeholder="energyUnits"/>
        <input id= rcashValue type="text" name="rcashValue" placeholder="cashValue"/>
        <input id= rcashUnits type="text" name="rcashUnits" placeholder="cashUnits"/>
        <button on:click={register_resident}>Register</button>
        <button on:click={get_resident}>Get Residents</button>
    </div>
</main>

<style>
main{
        margin: 0 auto;
    }
input, button{
    position: relative;
    top: 50%;
    /*left: 45%;
    display: block;*/
    z-index: 20;
}
/*
button{
    left: 49%;
}*/
</style>