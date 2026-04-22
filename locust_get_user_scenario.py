from locust import HttpUser, between, task
from tools.fakers import fake

class GetUserScenarioUser(HttpUser):
    wait_time = between(1, 3)
    user_data: dict

    def on_start(self) -> None:
        request = {
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "middle_name": fake.middle_name(),
            "phone_number": fake.phone_number()
        }
        respose = self.client.post("/api/v1/users", json=request)

        self.user_data = respose.json()

    @task
    def get_user(self):
        self.client.get(
            f"/api/v1/users/{self.user_data['user']['id']}",
            name="/api/v1/users/{user_id}",
        )