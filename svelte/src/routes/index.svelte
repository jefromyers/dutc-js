<svelte:head>
  <title>Hello</title>
</svelte:head>

<script>
import { onMount } from 'svelte';
import superagent from 'superagent';

let ws
onMount(async () => {
    ws = new WebSocket('ws://127.0.0.1:8000/ws');
    ws.onmessage = (msg) => {
        console.log(msg)
        ws.send('Hello there from Svelte')
    }
});

let title = 'Campaign'
function addCampaign(){
    superagent.post('http://127.0.0.1:8000/v1/campaigns/add')
                .send(JSON.stringify({title}))
                .then(res => {console.log(res.body)})
}
</script>

<h2>Howdy!</h2>

<input bind:value={title} type="text" />
<button on:click={addCampaign}>Add Campaign</button>
