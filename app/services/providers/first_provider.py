from typing import Any

import requests

from app.models.stay import Stay


class FirstProvider:
    def __init__(self):
        # check connection
        pass

    async def fetch_quote(self, stay: Stay) -> Any:
        # TODO: should make this async/await?
        req = requests.get('https://mocki.io/v1/3f79b51d-5c2c-4e2c-9f32-ddfe3398acdd')
        response = req.json()
        print("responseresponse", response)
        return response
