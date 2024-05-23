from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/test-betfair', methods=['GET'])
def test_betfair():
    try:
        # Replace with actual Betfair API endpoint and authentication details
        response = requests.get('https://api.betfair.com/exchange/betting/rest/v1.0/listEventTypes/', headers={
            'X-Application': 'your_app_key',
            'X-Authentication': 'your_session_token'
        })
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)