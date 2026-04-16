from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationResponseSchema,
    GetOperationReceiptResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryResponseSchema,
    MakeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema
)



class OperationsGatewayHTTPClient(HTTPClient):

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :return: get response
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Новый метод получения информации об операции по operation_id
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :return: get response
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Новый метод получения информации об операции по operation_id
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение операций по account_id
        """
        return self.get(
            url=f'/api/v1/operations',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Новый метод получения операций по account_id
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получение списка операций для определенного счета.
        :return: get response
        """
        return self.get(
            url=f'/api/v1/operations/operations-summary',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Новый метод получения списка операций для определенного счета.
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """"
        Создание операции комиссии
        :return: post response
        """
        return self.post(
            url=f'/api/v1/operations/make-fee-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Новый метод создания операции комиссии
        """
        request = MakeOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции пополнения
        :return: post response
        """
        return self.post(
            url=f'/api/v1/operations/make-top-up-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        Новый метод создания операции пополнения
        """
        request = MakeOperationRequestSchema(
            status="COMPLETED",
            amount=1055.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка
        :return: post response
        """
        return self.post(
            url=f'/api/v1/operations/make-cashback-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Новый метод создания операции кэшбэка
        """
        request = MakeOperationRequestSchema(
            status="COMPLETED",
            amount=1058.74,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)


    def make_transfer_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции перевода
        :return: post response
        """
        return self.post(
            url=f'/api/v1/operations/make-transfer-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Новый метод создания операции перевода
        """
        request = MakeOperationRequestSchema(
            status="FAILED",
            amount=50.74,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создание операции покупки
        :return: post response
        """
        return self.post(
            url=f'/api/v1/operations/make-purchase-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        Новый метод создание операции покупки
        """
        request = MakePurchaseOperationRequestSchema(
            status="COMPLETED",
            amount=78.74,
            card_id=card_id,
            account_id=account_id,
            category="goods"
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции оплаты по счету
        :return: post response
        """
        return self.post(
            url=f'/api/v1/operations/make-bill-payment-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Новый метод создание операции оплаты по счету
        """
        request = MakeOperationRequestSchema(
            status="FAILED",
            amount=70.85,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestSchema) -> Response:
        """
        Создание операции снятия наличных денег
        :return: post response
        """
        return self.post(url=f'/api/v1/operations/make-cash-withdrawal-operation', json=request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Новый метод создания операции снятия наличных денег
        """
        request = MakeOperationRequestSchema(
            status="COMPLETED",
            amount=78.74,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
