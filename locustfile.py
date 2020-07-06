from locust import HttpUser, task, constant


class WebsiteUser(HttpUser):
    wait_time = constant(1)

    @task(1)
    def view_get(self):
        self.client.get(
            url="/"
        )

    @task(2)
    def view_post(self):
        self.client.post(
            url="/items",
            headers={'content-type': 'application/json'},
            json={"id": 1, "name": "new_item"}
        )
