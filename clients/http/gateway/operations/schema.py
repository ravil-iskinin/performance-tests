from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from backports.strenum import StrEnum
from tools.fakers import fake

class OperationsStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationsType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class GetOperationsQuerySchema(BaseModel):
    """
    QueryParams для get запроса по операциям
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class MakeOperationRequestSchema(BaseModel):
    """
    RequestSchema для post запроса общий
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для make_fee
    """

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для make_top_up
    """

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для make_cashback
    """

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для make_transfer
    """

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для make_bill_payment
    """

class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для make_cash
    """

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    RequestSchema для запроса Создание операции оплаты по счету
    """
    category: str = Field(default_factory=fake.category)

class OperationSchema(BaseModel):
    """
    Вспомогательный класс
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationsType
    status: OperationsStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Вспомогательный класс
    """
    url: HttpUrl
    document: str

class OperationsSummarySchema(BaseModel):
    """
    Вспомогательный класс
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationsResponseSchema(BaseModel):
    """
    Класс ответа для операциq
    """
    operations: list[OperationSchema]

class GetOperationResponseSchema(BaseModel):
    """
    Класс ответа для операции
    """
    operation: OperationSchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Класс ответа для операции по чеку
    """
    receipt: OperationReceiptSchema


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Класс ответа по списку операций
    """
    summary: OperationsSummarySchema

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Класс ответа по выплате
    """
    operation: OperationSchema

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Класс ответа пополнения счета
    """
    operation: OperationSchema

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Класс ответа пополнения по кэшбеку
    """
    operation: OperationSchema

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Класс ответа пополнения по трансферу
    """
    operation: OperationSchema

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Класс ответа пополнения по покупки
    """
    operation: OperationSchema

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Класс ответа пополнения по счету
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Класс ответа пополнения с помощью наличных
    """
    operation: OperationSchema
