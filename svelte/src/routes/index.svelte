<svelte:head>
  <title>Hello</title>
</svelte:head>

<script>
import { onMount } from 'svelte';

let ws
onMount(async () => {
    ws = new WebSocket('ws://127.0.0.1:8000/ws');
    ws.onmessage = (msg) => {
        console.log('Server says: ' + msg)
        ws.send('Hello there from Svelte')
    }
});
</script>

<h2>Howdy!</h2>
