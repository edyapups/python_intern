import pytest
from app.utils import is_alive_host
from tests.base import MockClientSession


@pytest.mark.asyncio
@pytest.mark.parametrize('status_code,throw_error,expected',
                         [
                             (0, False, False),
                             (99, False, False),
                             (100, False, True),
                             (200, False, True),
                             (400, False, True),
                             (401, False, False),
                             (200, True, False),
                         ])
async def test_alive_host(status_code, throw_error, expected):
    client = MockClientSession(status_code, throw_error)
    result = await is_alive_host('test', client)

    assert result == expected
