from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_response(question):
    api_key = "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"
    endpoint = "https://azeu-api-beta.onrender.com/GlobalGPT"
    params = {"question": question, "apiKey": api_key}

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch response."}

@app.route('/')
def index():
    return 'Hello, please go to /ask to ask a question.'

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form['question']
        response = get_response(question)
        return jsonify(response)
    else:
        return 'Please use POST method to ask a question.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

