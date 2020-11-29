import fastapi
from app.utils import is_alive_host
from aiohttp import ClientSession


class FastAPI(fastapi.FastAPI):
    client: ClientSession
    healthz_returns = {
        True: 'up',
        False: 'down',
    }


app = FastAPI()


@app.on_event('startup')
async def open_client_session():
    """
    Initializes a session for outgoing requests when the application starts.
    """
    app.client = ClientSession()


@app.get('/healthz')
async def healthz(hostname: str):
    """
    Returns:
        {
            'status': on | off
        }

    up: if the received host returns http status between 100 and 400.
    down: otherwise.
    """
    result = await is_alive_host(hostname, app.client)
    return {
        'status': app.healthz_returns[result],
    }


@app.on_event('shutdown')
async def close_client_session():
    """
    Closes the session for outgoing requests when the application stops.
    """
    await app.client.close()
