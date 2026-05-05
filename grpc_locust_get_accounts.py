from locust import User, between, task
from clients.grpc.gateway.locust import GatewayGRPCTaskSet


from contracts.services.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountResponse
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsResponse




class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный сценарий, который последовательно:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счет.
    3. Получает все счета.

    Использует базовый GatewayGRPCTaskSet и уже созданных в нём API клиентов.
    """

    create_user_response: CreateUserResponse | None = None
    open_deposit_account_response: OpenDepositAccountResponse | None = None
    get_accounts_response: GetAccountsResponse | None = None

    @task(2)
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        if not self.create_user_response:
            return
        self.open_deposit_account_response = self.accounts_gateway_client.open_deposit_account(
            user_id=self.create_user_response.user.id
        )

    @task(6)
    def get_accounts(self):
        if not self.create_user_response:
            return
        self.get_accounts_response = self.accounts_gateway_client.get_accounts(
            user_id=self.create_user_response.user.id
        )

class GetDocumentsScenarioUser(User):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения документов.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)

