from typing import Any

from models.stay import Stay


class FirstProvider:
    def __init__(self):
        # check connection
        pass

    def fetch_quote(self, stay: Stay) -> Any:
        return {'aa': 123}
