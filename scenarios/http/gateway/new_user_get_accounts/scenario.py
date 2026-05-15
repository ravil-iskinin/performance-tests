from locust import task
from clients.http.gateway.locust import GatewayHTTPTaskSet
from tools.locust.user import LocustBaseUser

from clients.http.gateway.users.schema import CreateUserResponseSchema

class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    Нагрузочный сценарий, который последовательно:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счет.
    3. Получает все счета.

    Использует базовый GatewayHTTPTaskSet и уже созданных в нём API клиентов.
    """
    create_user_response: CreateUserResponseSchema | None = None

    @task(2)
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        if not self.create_user_response:
            return
        self.accounts_gateway_client.open_deposit_account(self.create_user_response.user.id)

    @task(6)
    def get_accounts(self):
        if not self.create_user_response:
            return
        self.accounts_gateway_client.get_accounts(self.create_user_response.user.id)


class GetDocumentsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения документов.
    """
    tasks = [GetAccountsTaskSet]
