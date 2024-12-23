from locust import HttpUser , task, between

#  模拟用户行为
class user(HttpUser):
    wait_time = between(1, 3)

    @task
    def translate(self):
        self.client.get("/translate/Hello%20how%20are%20you.")

