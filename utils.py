from aiohttp import ClientSession


async def is_alive_host(hostname: str, client: ClientSession) -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    result = await client.get(hostname)
    return 100 <= result.status <= 400
