import requests


class HttpManager:
    @staticmethod
    def get(url: str):
        result = requests.get(url)
        return result
