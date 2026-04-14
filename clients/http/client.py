from httpx import Client, URL, QueryParams, Response
from typing import Union, Optional, Any

class HTTPClient:
    def __init__(self, client: Client):
        self.client = client
    def get(self, url: Union[URL, str], params: Optional[QueryParams] = None) -> Response:
        return self.client.get(url, params=params)

    def post(self, url: Union[URL, str], json: Optional[Any] = None) -> Response:
        return  self.client.post(url, json=json)


