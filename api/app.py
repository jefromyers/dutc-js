import logging
from random import choice
from string import ascii_lowercase 

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def ping(request):
    ''' Signs of life '''

    return JSONResponse(
        {'ping': 'pong'}, 
        headers = {"Access-Control-Allow-Origin": 'http://127.0.0.1:3000'}
    )

async def ws_index(ws):
    await ws.accept()
    await ws.send_text('sup')
    while True:
        msg = await ws.receive_text()
        logger.info(f'Message from client: {msg}')
    await websocket.close()

routes = [
    WebSocketRoute("/ws", endpoint=ws_index),
    Route("/", endpoint=ping, methods=["GET"]),
]

app = Starlette(routes=routes,)
