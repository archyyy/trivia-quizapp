import requests


class Question:
    def __init__(self) -> None:
        # Request API
        self.response = requests.get(
            url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"
        )
        self.results = self.response.json()["results"]

