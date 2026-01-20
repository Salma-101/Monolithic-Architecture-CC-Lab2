from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_events(self):
        # i used params instead of hardcoding query string
        self.client.get("/events", params={"user": "locust_user"})
