import httpx
import time

# Создание и получение пользователя
create_user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

try:
    create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
    create_user_response_data = create_user_response.json()
    print("Create user response:", create_user_response_data)
    print("Status code:", create_user_response.status_code)
except Exception as e:
    print("Error: create user {e}")

try:
    get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{create_user_response_data['user']['id']}")
    get_user_response_data = get_user_response.json()
    print("Get user response:", get_user_response_data)
    print("Status code:", get_user_response.status_code)
except Exception as e:
    print("Error: get user {e}")

# Создание и получение депозита
open_deposit_account_payload = {
  "userId": create_user_response_data['user']['id']
}

try:
    create_open_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",
                                                      json=open_deposit_account_payload)
    create_open_deposit_account_data = create_open_deposit_account_response.json()
    print("Create OpenDepositAccount response:", create_open_deposit_account_data)
    print("Status code:", create_open_deposit_account_response.status_code)
except Exception as e:
    print("Error: create open deposit accounts {e}")

try:
    get_open_deposit_account_response = httpx.get("http://localhost:8003/api/v1/accounts",
                                                  params=open_deposit_account_payload)
    get_open_deposit_account_data = get_open_deposit_account_response.json()
    print("Create OpenDepositAccount response:", get_open_deposit_account_data)
    print("Status code:", get_open_deposit_account_response.status_code)
except Exception as e:
    print("Error: get open deposit accounts {e}")

