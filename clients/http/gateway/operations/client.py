from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

class GetOperationsQueryDict(TypedDict):
    """
    QueryParams для get запроса по операциям
    """
    accountId: str

class MakeOperationRequestDict(TypedDict):
    """
    RequestDict для post запроса общий
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    RequestDict для запроса  Создание операции оплаты по счету
    """
    category: str

class OperationsGatewayHTTPClient(HTTPClient):

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :return: get response
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :return: get response
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:

        """
        Получение чека по операции по operation_id
        :return: get response
        """
        return self.get(url=f'/api/v1/operations', params=query)

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.
        :return: get response
        """
        return self.get(url=f'/api/v1/operations/operations-summary', params=query)

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """"
        Создание операции комиссии
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-fee-operation', json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции пополнения
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make_top_up_operation', json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make_cashback_operation', json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции перевода
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make_transfer_operation', json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make_purchase_operation', json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make_bill_payment_operation', json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make_cash_withdrawal_operation', json=request)











