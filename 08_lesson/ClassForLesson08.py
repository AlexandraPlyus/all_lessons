import requests


class GetKey:
    def __init__(self, base_url):
        self.url = base_url

    def get_key(self):
        body = {"login": "???", "password": "???"}
        respone = requests.post(
            f"{self.url}/api-v2/auth/keys/get", json=body
        ).json()
        key = respone[0]["key"]
        return key
