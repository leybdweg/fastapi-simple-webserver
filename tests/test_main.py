# import sys
# import os

import pytest
from httpx import AsyncClient, ASGITransport

from di import availableStays
from models.stay import Stay

# FIXME: it doesnt work otherise ( ModuleNotFoundError: No module named 'main')
# Add the parent directory to the Python path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from fastapi.testclient import TestClient

from main import app


# TODO: how to put this globally? import?
@pytest.fixture
def anyio_backend():
    return 'asyncio'


client = TestClient(app)


class TestSearchAPI:
    request_id = ""

    def setup_method(self):
        stay = Stay(
            request_id="abc-def",
            ski_site=2,
            from_date="10-10-2030",
            to_date="12-10-2030",
            group_size=5,
        )
        availableStays.available_stays_offers = [stay]

    @pytest.mark.anyio
    async def test_not_found_search(self):
        async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            response = await ac.get("/search", params={"request_id": "doesnt-exist"})
        assert response.json() is None

    @pytest.mark.anyio
    async def test_add_stay(self):
        async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            body = {
                "ski_site": 2,
                "from_date": "09-10-2030",
                "to_date": "12-10-2030",
                "group_size": 5,
            }
            response = await ac.post("/search", json=body)
        output = response.json()
        print('rrequestId', output)
        assert isinstance(output, str)
        self.request_id = output

    @pytest.mark.anyio
    async def test_found_search(self):
        async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            response = await ac.get("/search", params={"request_id": 'abc-def'})
        assert response.json() == {
            "request_id": "abc-def",
            "ski_site": 2,
            "from_date": "10-10-2030",
            "to_date": "12-10-2030",
            "group_size": 5,
            "provider_datas": {}
        }
