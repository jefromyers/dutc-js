import logging
from dataclasses import dataclass, field
import sqlalchemy
from contextlib import contextmanager
from random import choice
from string import ascii_lowercase 

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.routing import WebSocketRoute
from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket, WebSocketState
from database import SessionLocal, engine, Base, Campaign

Base.metadata.create_all(bind=engine)

logger = logging.getLogger("uvicorn")

@contextmanager
def session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@dataclass
class SocketPool:
    pool:set = field(default_factory=set) 

    def add(self, connection):
        ''' Add a connected WebSocket to the pool '''
        self.pool.add(connection)

    def remove(self, connection):
        ''' Remove a connected WebSocket to the pool '''
        self.pool.remove(connection)

    async def broadcast_all(self, msg):
        ''' Broadcast to everyone in the pool if they're connected '''

        for c in self.pool:
            if c.client_state == WebSocketState.CONNECTED:
                await c.send_text(msg)

    def __len__(self):
        return len(self.pool)

Pool = SocketPool()

class Socket(WebSocketEndpoint):
    encoding = "text"
    
    async def on_connect(self, websocket):
        await websocket.accept()
        Pool.add(websocket)
        logger.info(f'Added WebSocket connetion to Pool, size is now {len(Pool)}')

    async def on_receive(self, websocket, data):
        logger.info(f'Recieved: {data}')

    async def on_disconnect(self, websocket, close_code):
        Pool.remove(websocket)
        logger.info(f'Removed WebSocket connetion from Pool, size is now {len(Pool)}')

async def ping(request):
    ''' Signs of life '''
    
    # await Pool.broadcast_all("woop")
    logger.info(f'Connections: {len(Pool)}')
    return JSONResponse(
        {'ping': 'pong', 'connections': len(Pool)}, 
        # headers = {"Access-Control-Allow-Origin": request.headers['Origin']}
    )

async def send_all(request):
    ''' Signs of life '''
    
    await Pool.broadcast_all("woop")
    return JSONResponse(
        {'ping': 'pong', 'connections': len(Pool)}, 
        # headers = {"Access-Control-Allow-Origin": request.headers['Origin']}
    )

async def add_campaign(request):
    ''' Add a Campaign '''

    try:
        payload = await request.json()
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Uable to parse request")
    
    title = payload.get('title')
    if not title:
        raise HTTPException(status_code=400, detail="Must provide a Campaign name")
    
    with session() as s:
        campaign = Campaign(title=title)
        s.add(campaign)
        s.commit()
        s.refresh(campaign)

    return JSONResponse(
        {'Created': f'{campaign.id} - {campaign.title}'}, 
        headers = {"Access-Control-Allow-Origin": request.headers['Origin']}
    )


routes = [
    WebSocketRoute("/ws", Socket),
    Route("/", endpoint=ping, methods=["GET"]),
    Route("/send", endpoint=send_all, methods=["GET"]),
    Route("/v1/campaigns/add", endpoint=add_campaign, methods=["POST"]),
]

app = Starlette(
    routes=routes,
)
