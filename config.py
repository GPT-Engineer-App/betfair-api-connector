import os

class Config:
    BETFAIR_APP_KEY = os.getenv('BETFAIR_APP_KEY')
    BETFAIR_SESSION_TOKEN = os.getenv('BETFAIR_SESSION_TOKEN')