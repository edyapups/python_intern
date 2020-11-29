import pytest
from app.main import app
from httpx import AsyncClient
from tests.base import MockClientSession, init_client


@pytest.mark.asyncio
@pytest.mark.parametrize('status_code,throw_error,expected',
                         [
                             (0, False, 'down'),
                             (99, False, 'down'),
                             (100, False, 'up'),
                             (200, False, 'up'),
                             (400, False, 'up'),
                             (401, False, 'down'),
                             (200, True, 'down'),
                         ])
async def test_mocked_host(status_code, throw_error, expected):
    app.client = MockClientSession(status_code, throw_error)
    async with AsyncClient(app=app, base_url='http://test') as client:
        result = await client.get('/healthz', params={'hostname': 'test'})

    assert 'status' in result.json()
    assert result.json()['status'] == expected


@pytest.mark.asyncio
@pytest.mark.parametrize('hostname,expected',
                         [
                             ('google.com', 'up'),
                             ('test', 'down'),
                         ])
async def test_host(init_client, hostname, expected):
    app.client = init_client
    async with AsyncClient(app=app, base_url='http://test') as client:
        result = await client.get('/healthz', params={'hostname': hostname})

    assert 'status' in result.json()
    assert result.json()['status'] == expected
