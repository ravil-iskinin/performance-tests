import time
import httpx

def create_user(payload):
    """
    Создание пользователя
    :return: json ответ
    """
    try:
        response = httpx.post("http://localhost:8003/api/v1/users", json=payload)
        data = response.json()
        print("Create user response:", data)
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error: create user {e}")

    return data


def create_open_credit_card_account(payload):
    """
    Создание кредитного счета и карты
    :return: json ответ
    """
    try:
        response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                              json=payload)
        data = response.json()
        print("Create open credit card account response:", data)
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error: create open credit card account {e}")

    return data


def create_make_purchase_operation(payload):
    """
    Выполнение операции
    :return: json ответ
    """
    try:
        response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                              json=payload)
        data = response.json()
        print("Create operation response:", data)
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error: create operation {e}")

    return data

def get_open_credit_card_account(payload):
    """
    Получение инф-ции по кредитной карте
    :param data:
    :return:
    """
    try:
        response = httpx.get(f"http://localhost:8003/api/v1/accounts",
                             params=payload)
        data = response.json()
        print("Get open credit card account response:", data)
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error: get open credit card account {e}")


def get_user(data):
    """
    Получение инф-ции по пользователю
    :return:
    """
    try:
        response = httpx.get(f"http://localhost:8003/api/v1/users/{data['user']['id']}")
        data = response.json()
        print("Get user response:", data)
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error: get user {e}")


def get_operation_receipt(operation_id):
    """
    Получение счета
    :return:
    """
    try:
        response = httpx.get(f"http://localhost:8003/api/v1/operations/{operation_id}")
        data = response.json()
        print("Get operation_receip response:", data)
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error: get operation receip {e}")

if __name__ == "__main__":
    create_user_payload = {
        "email": f"user{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"
    }
    data_create_user = create_user(create_user_payload)
    get_user(data_create_user)

    open_credit_card_accoun_payload = {
        "userId": data_create_user['user']['id']
    }

    data_create_open_credit_card_accoun =  create_open_credit_card_account(open_credit_card_accoun_payload)
    get_open_credit_card_account(open_credit_card_accoun_payload)

    make_purchase_operation_payload = {
        "status": "IN_PROGRESS",
        "amount": 77.99,
        "category": "taxi",
        "cardId": data_create_open_credit_card_accoun["account"]["cards"][0]["id"],
        "accountId": data_create_open_credit_card_accoun["account"]["id"]
    }

    data_create_make_purchase_operation= create_make_purchase_operation(make_purchase_operation_payload)
    path_operation_id = data_create_make_purchase_operation["operation"]["id"]
    get_operation_receipt(path_operation_id)
