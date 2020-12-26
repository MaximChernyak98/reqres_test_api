import requests


class HttpManager:
    @staticmethod
    def post(url: str, json):
        result = requests.post(url, json)
        return result
