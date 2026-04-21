from grpc import Channel
from tools.fakers import fake
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.operations.operation_pb2 import OperationStatus
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse
)
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import  (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import  (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse
)

class OperationsGatewayGRPCClient(GRPCClient):
    def __init__(self, channel: Channel):
        """
        gRPC-клиент для взаимодействия с OperationsGatewayService.
        Предоставляет высокоуровневые методы для работы со счетами.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Получение информации об операции по operation_id
        """
        return self.stub.GetOperation(request)

    def get_operation(self, operation_id: str)-> GetOperationResponse:
        """
        Новый метод информации об операции по operation_id
        """
        request = GetOperationRequest(operation_id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Получение чека по операции по operation_id
        """
        return self.stub.GetOperationReceipt(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Новый метод получение чека по операции по operation_id
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_ap(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Получение списка операций для определенного счета.
        """
        return self.stub.GetOperations(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Новый метод получение списка операций для определенного счета.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Получение статистики по операциям для определенного счета.
        """
        return self.stub.GetOperationsSummary(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Новый метод получение статистики по операциям для определенного счета.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Создание операции комиссии
        """
        return self.stub.MakeFeeOperation(request)

    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponse:
        """
        Новый метод создание операции комиссии
        """
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Создание операции пополнения
        """
        return self.stub.MakeTopUpOperation(request)

    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponse:
        """
        Новый метод создание операции пополнения
        """
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Создание операции кэшбэка
        """
        return self.stub.MakeCashbackOperation(request)

    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponse:
        """
        Новый метод создание операции кэшбэка
        """
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id
        )
        return self.make_cashback_operation.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Создание операции перевода
        """
        return self.stub.MakeTransferOperation(request)

    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponse:
        """
        Новый метод создание операции перевода
        """
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Создание операции покупки
        """
        return self.stub.MakePurchaseOperation(request)

    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponse:
        """
        Новый метод создание операции покупки
        """
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id,
            category=fake.category()
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Создание операции оплаты по счету
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponse:
        """
        Новый метод создание операции оплаты по счету
        """
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Создание операции снятия наличных денег
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def make_cash_withdrawal_operation(self, account_id: str, card_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Новый метод операции снятия наличных денег
        """
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            account_id=account_id,
            card_id=card_id
        )
        return self.make_cash_withdrawal_operation_api(request)

def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())