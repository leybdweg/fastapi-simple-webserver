import pytest

from app.di import availableStays
from app.models.stay import Stay

from fastapi.testclient import TestClient

from main import app


# TODO: how to put this globally? import?
@pytest.fixture
def anyio_backend():
    return 'asyncio'


client = TestClient(app)


class TestBackground:
    stay = Stay(
        request_id="abc-def",
        ski_site=2,
        from_date="10-10-2030",
        to_date="12-10-2030",
        group_size=5,
    )

    def setup_method(self):
        availableStays.available_stays_offers = [self.stay]

    @pytest.mark.anyio
    async def test_providers_data_was_updated(self, mocker):
        mock_data = {"mocked": 123}

        # Mock requests.get
        mock_get = mocker.patch("requests.get")
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data

        await availableStays.update_quotes()

        expected_data = {
            'first': {'mocked': 123},
            'second': None
        }
        assert availableStays.available_stays_offers[0].provider_datas == expected_data
