from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict
from clients.http.gateway.client import build_gateway_http_client

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
    RequestDict для запроса Создание операции оплаты по счету
    """
    category: str

class OperationDict(TypedDict):
    """
    Вспомогательный класс
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Вспомогательный класс
    """
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Вспомогательный класс
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsResponseDict(TypedDict):
    """
    Класс ответа для операциq
    """
    operations: list[OperationDict]

class GetOperationResponseDict(TypedDict):
    """
    Класс ответа для операции
    """
    operation: OperationDict

class GetOperationReceiptResponseDict(TypedDict):
    """
    Класс ответа для операции по чеку
    """
    receipt: OperationReceiptDict


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Класс ответа по списку операций
    """
    summary: OperationsSummaryDict

class MakeFeeOperationResponseDict(TypedDict):
    """
    Класс ответа по выплате
    """
    operation: OperationDict

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Класс ответа пополнения счета
    """
    operation: OperationDict

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Класс ответа пополнения по кэшбеку
    """
    operation: OperationDict

class MakeTransferOperationResponseDict(TypedDict):
    """
    Класс ответа пополнения по трансферу
    """
    operation: OperationDict

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Класс ответа пополнения по покупки
    """
    operation: OperationDict

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Класс ответа пополнения по счету
    """
    operation: OperationDict

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Класс ответа пополнения с помощью наличных
    """
    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :return: get response
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Новый метод получения информации об операции по operation_id
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :return: get response
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Новый метод получения информации об операции по operation_id
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение операций по account_id
        """
        return self.get(url=f'/api/v1/operations', params=query)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Новый метод получения операций по account_id
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations(query)
        return response.json()

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.
        :return: get response
        """
        return self.get(url=f'/api/v1/operations/operations-summary', params=query)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Новый метод получения списка операций для определенного счета.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """"
        Создание операции комиссии
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-fee-operation', json=request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Новый метод создания операции комиссии
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции пополнения
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-top-up-operation', json=request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Новый метод создания операции пополнения
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=1055.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-cashback-operation', json=request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Новый метод создания операции кэшбэка
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=1058.74,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()


    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции перевода
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-transfer-operation', json=request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Новый метод создания операции перевода
        """
        request = MakeOperationRequestDict(
            status="FAILED",
            amount=50.74,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-purchase-operation', json=request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        Новый метод создание операции покупки
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=78.74,
            cardId=card_id,
            accountId=account_id,
            category="goods"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-bill-payment-operation', json=request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Новый метод создание операции оплаты по счету
        """
        request = MakeOperationRequestDict(
            status="FAILED",
            amount=70.85,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-cash-withdrawal-operation', json=request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Новый метод создания операции снятия наличных денег
        """
        request = MakeOperationRequestDict(
            status="COMPLETED",
            amount=78.74,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
