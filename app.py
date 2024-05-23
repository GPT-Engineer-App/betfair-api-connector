from flask import Flask, jsonify
import requests
from betfair_api import BetfairAPI
from config import Config

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask Betfair API Integration!"})

@app.route('/betfair/event-types')
def betfair_event_types():
    betfair = BetfairAPI(Config.BETFAIR_APP_KEY, Config.BETFAIR_SESSION_TOKEN)
    event_types = betfair.list_event_types()
    return jsonify(event_types)

if __name__ == '__main__':
    app.run(debug=True)