import pytest
from app.app import app
from httpx import AsyncClient


class MockResponse:
    status: int

    def __init__(self, status):
        self.status = status


class MockClientSession:
    response_status: int = 200

    async def get(self, *args, **kwargs):
        return MockResponse(self.response_status)


app.client = MockClientSession()


@pytest.mark.asyncio
@pytest.mark.parametrize('status_code,expected',
                         [
                             (0, 'down'),
                             (99, 'down'),
                             (100, 'up'),
                             (200, 'up'),
                             (400, 'up'),
                             (401, 'down'),
                         ])
async def test_alive_host(status_code, expected):
    app.client.response_status = status_code
    async with AsyncClient(app=app, base_url='http://test') as client:
        result = await client.get('/healthz', params={'hostname': 'test'})

    assert 'status' in result.json()
    assert result.json()['status'] == expected
