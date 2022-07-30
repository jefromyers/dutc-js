import logging
import sqlalchemy
from contextlib import contextmanager
from random import choice
from string import ascii_lowercase 

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket
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

def ping(request):
    ''' Signs of life '''

    return JSONResponse(
        {'ping': 'pong'}, 
        headers = {"Access-Control-Allow-Origin": '*'}
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
        headers = {"Access-Control-Allow-Origin": '*'}
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
    Route("/v1/campaigns/add", endpoint=add_campaign, methods=["POST"]),
]

app = Starlette(
    routes=routes,
)
