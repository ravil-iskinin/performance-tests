from gevent.pool import Group
from locust import HttpUser, between, task
from tools.fakers import fake

class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(1, 3)
    used_data: dict


    def on_start(self) -> None:
        request = {
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.middle_name(),
            "phone_number": fake.phone_number()
        }
        respose = self.client.post("/api/v1/users", json=request)
        self.used_data = respose.json()


    @task
    def open_debit_card_account(self):
        request = {
            "userId": self.used_data['user']['id']
        }
        self.client.post("/api/v1/accounts/open-debit-card-account", json=request)

