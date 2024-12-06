import pytest
from httpx import AsyncClient, ASGITransport

from app.di import availableStays
from app.models.stay import Stay

from fastapi.testclient import TestClient

from main import app


# TODO: how to put this globally? import?
@pytest.fixture
def anyio_backend():
    return 'asyncio'


client = TestClient(app)


class TestSearchAPI:

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
        assert isinstance(output['request_id'], str) # TODO: check if it's uuid format?
        expected_output = {'ski_site': 2, 'from_date': '09-10-2030', 'to_date': '12-10-2030', 'group_size': 5, 'provider_datas': {}}
        testable_output = {**output}
        del testable_output['request_id'] # dynamic value, cant be easily tested
        assert testable_output == expected_output

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
