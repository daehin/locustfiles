from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task
    def get_domain_classifier_status(self):
        self.client.get("/auracognitive/v1//domain_classifier/status", name="/domain_classifier/status")

    @task
    def get_suggestion_status(self):
        self.client.get("/auracognitive/v1//suggestion/status", name="/suggestion/status")

    @task
    def get_insights_resolution_status(self):
        self.client.get("/auracognitive/v1//insights_resolution/status", name="/insights_resolution/status")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 3000
    host = "https://changeThisForRealHost.es:8000"

