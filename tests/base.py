from aiohttp.client_exceptions import ClientError


class MockResponse:
    status: int

    def __init__(self, status_code: int = 200):
        self.status = status_code


class MockClientSession:
    def __init__(self, status_code: int = 200, throw_error: bool = False):
        self.throw_error = throw_error
        self.status_code = status_code

    async def get(self, hostname):
        if self.throw_error:
            raise ClientError
        return MockResponse(self.status_code)
