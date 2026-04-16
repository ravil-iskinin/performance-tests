from pydantic import BaseModel, HttpUrl

class DocumentSchema(BaseModel):
    """
    Общий объект
    """
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Для ответа по тарифу
    """

    tariff: DocumentSchema

class GetСontractDocumentResponseSchema(BaseModel):
    """
    Для ответа по контракту
    """
    contract: DocumentSchema


