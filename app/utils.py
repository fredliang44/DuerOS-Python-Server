import requests

class Verify:
    def __init__(self, url):
        self.url = url

    def get_certs(self):
        r = requests.get(self.url)
        print(r.text)
