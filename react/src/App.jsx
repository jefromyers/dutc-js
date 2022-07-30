const App = () => {

    const ws = new WebSocket('ws://127.0.0.1:8000/ws');
    
    ws.onmessage = (msg) => {
        console.log('Server says: ' + msg)
        ws.send('Hello there')
    }
    
    return (
        <h4>App</h4>
    )
}

export default App

