from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError


async def is_alive_host(hostname: str, client: ClientSession) -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    try:
        result = await client.get('http://' + hostname)
        return 100 <= result.status <= 400
    except ClientError:
        return False
