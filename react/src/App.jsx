import { useRef } from 'react'
import superagent from 'superagent';


const App = () => {

    const campaignName = useRef(null)
    const createCampaign = () => {
        superagent.post('http://127.0.0.1:8000/v1/campaigns/add')
                  .send(JSON.stringify({ title: campaignName.current.value }))
                  .then(res => {console.log(res.body)})
    }

    const ws = new WebSocket('ws://127.0.0.1:8000/ws');
    ws.onmessage = (msg) => {
        console.log('Server says: ' + msg)
        ws.send('Hello there')
    }
    
    return (
        <>
        <h4>App</h4>
        <input ref={campaignName} type="text" placeholder="Campaign Name" />
        <button onClick={createCampaign}>Add Campaign</button>
        </>
    )
}

export default App

