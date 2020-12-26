import requests


class HttpManager:
    @staticmethod
    def post(url: str):
        result = requests.post(url)
        return result
