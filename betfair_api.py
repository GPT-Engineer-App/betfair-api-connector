import requests

class BetfairAPI:
    def __init__(self, app_key, session_token):
        self.base_url = "https://api.betfair.com/exchange/betting/rest/v1.0/"
        self.app_key = app_key
        self.session_token = session_token

    def get_headers(self):
        return {
            'X-Application': self.app_key,
            'X-Authentication': self.session_token,
            'Content-Type': 'application/json'
        }

    def list_event_types(self):
        url = self.base_url + "listEventTypes/"
        response = requests.post(url, headers=self.get_headers(), json={})
        return response.json()