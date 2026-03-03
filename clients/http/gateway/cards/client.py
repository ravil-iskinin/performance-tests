from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

class CreateCardRequestDict(TypedDict):
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards/issue-virtual-card  и
    /api/v1/cards/issue-physical-card сервиса http-gateway.
    """
    def issue_virtual_card_api(self, request) -> Response:
        """
        Создание виртуальной карты.


        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера (объект httpx.Response).

        :param request:
        :return:
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request):
        """
        Создание физической карты.


        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f" /api/v1/cards/issue-physical-card",  json=request)
