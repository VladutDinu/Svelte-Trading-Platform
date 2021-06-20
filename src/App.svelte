<script>
import Book from "./Book.svelte";
import LeftPanel from "./LeftPanel.svelte";
import RightLower from "./Right-lower.svelte";
import RigthUpper from "./Rigth-upper.svelte";
import Login from "./Login.svelte";
</script>

<main>
	<div class="Upper-panel">
		<p>PNH</p>
	</div>
	<div class="Left-panel">
		<LeftPanel></LeftPanel>
	</div>
	<div class="panels">
		<div class="Right-panel1">
			<RigthUpper></RigthUpper>
		</div>
		<div class="Right-panel2">
			<!--<RightLower yaxis={'Y axis title form app.svelte which is nice'}></RightLower>-->
			<Login></Login>
		</div>
	</div>
</main>

<style>
	main {
		text-align: center;
		max-width: 240px;
		margin: 0 auto;
	}
	.Upper-panel {
		border: 4px solid;
	}
	.panels{
		display: block;
	}
	.panels div:not(:last-child){
		border-bottom: none; /* Prevent double borders */
	}
	.Left-panel {
		height: 92%;
		width: 15%;
		position: fixed;
		left: 0;
		text-align: left;
		background-color: #ff3e00;
	}
	.Right-panel1 {
		height: 43%;
		width: 85%;
		position: fixed;
		overflow-x: hidden;
		overflow-y: hidden;
		right: 0;
		text-align: left;
		background-color: darkgoldenrod;
	}
	.Right-panel2 {
		height: 49%;
		width: 85%;
		position: fixed;
		overflow-x: hidden;
		overflow-y: hidden;
		right: 0;
		bottom: 13px;
		text-align: left;
		background-color: darkkhaki;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
	
</style>