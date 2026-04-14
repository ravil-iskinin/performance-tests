from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

# # Открыть кредитный счет
accounts_gateway_client = accounts_gateway_client.open_debit_card_account(user_id=create_user_response['user']['id'])
print('Open credit card:', accounts_gateway_client)

# Получить документ тарифа
document_tariff = documents_gateway_client.get_tariff_document(account_id=accounts_gateway_client['account']['id'])
print('Get tariff document:', document_tariff)

# Получить документ контракта
document_contract = documents_gateway_client.get_contract_document(account_id=accounts_gateway_client['account']['id'])
print('Get contract document:', document_contract)
