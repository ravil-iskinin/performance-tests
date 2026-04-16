"""
{
  "accounts": [
    {
      "id": "string",
      "type": "UNSPECIFIED",
      "cards": [
        {
          "id": "string",
          "pin": "string",
          "cvv": "string",
          "type": "UNSPECIFIED",
          "status": "UNSPECIFIED",
          "accountId": "string",
          "cardNumber": "string",
          "cardHolder": "string",
          "expiryDate": "2025-06-08",
          "paymentSystem": "UNSPECIFIED"
        }
      ],
      "status": "UNSPECIFIED",
      "balance": 0
    }
  ]
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
from datetime import date


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str

try:
    tariff = DocumentSchema(
        url="localhost",
        document="doc data"
    )
except ValidationError as error:
    print(error.errors())


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str =  Field(alias="phoneNumber")


print(UserSchema(id="sdsa", email="adsfbae@gmail.com", lastName="sfbh", firstName="abhaeba", middleName="adfbnaenaqt", phoneNumber="WRBrbn"))



class CardSchema(BaseModel):
    id: str = "card-id"
    pin: str = "1234"
    cvv: str = "123"
    type: str = "PHYSICAL"
    status: str = "ACTIVE"
    account_id: str = Field(alias="accountId", default="account-id")
    card_number: str = Field(alias="cardNumber", default="123456789123456")
    card_holder: str = Field(alias="cardHolder", default="Bob Smith")
    expiry_date: date = Field(alias="expiryDate", default=date(2027,7, 10))
    payment_system: str = Field(alias="paymentSystem", default="VISA")


class AccountSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = 'CREDIT_CARD'
    cards: list[CardSchema] = Field(default_factory=list)
    status: str = "ACTIVE"
    balance: float = 2500

    def get_account_name(self) -> str:
        return f"{self.status} {self.type}"

account_1 = AccountSchema()
account_2 = AccountSchema()
print(account_1)
print(account_2)

account_dict = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            # "status": "ACTIVE",
            # "accountId": "account-id",
            # "cardNumber": "123456789123456",
            # "cardHolder": "Bob Smith",
            # "expiryDate": date(2027,7, 10),
            # "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 10.758
}

account_dict_model = AccountSchema(**account_dict)
# print('Account dict model:', account_dict_model)
# print(account_dict_model.model_dump(by_alias=True))


account_json = """
{
    "id": "account-id",
    "type": "CREDIT_CARD",
    "cards": [
        {
            "id": "card-id",
            "pin": "1234",
            "cvv": "123",
            "type": "PHYSICAL",
            "status": "ACTIVE",
            "accountId": "account-id",
            "cardNumber": "123456789123456",
            "cardHolder": "Bob Smith",
            "expiryDate": "2027-03-07",
            "paymentSystem": "VISA"
        }
    ],
    "status": "ACTIVE",
    "balance": 10.758
}
"""
#account_json_model = AccountSchema.model_validate_json(account_json)
#print('Account JSON model:', account_dict_model)