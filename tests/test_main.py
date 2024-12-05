import sys
import os

import pytest
from httpx import AsyncClient, ASGITransport

# FIXME: it doesnt work otherise ( ModuleNotFoundError: No module named 'main')
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.mark.anyio
async def test_not_found_search():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/search", params={"request_id": "doesnt-exist"})
    assert response.json() is None
