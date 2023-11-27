# main.py
from flask import Flask, request, jsonify
import chatbot_core

app = Flask(__name__)

@app.route('/', methods=['POST'])
def alorica_chatbot():
    request_json = request.get_json(silent=True)
    if request_json and 'queryResult' in request_json:
        response = chatbot_core.process_chatbot_request(request_json)
        return jsonify(response)
    else:
        return jsonify({"fulfillmentText": "No valid input received"})

# For Google Cloud Functions, define a function that accepts a request parameter
def gcf_alorica_chatbot(request):
    return alorica_chatbot()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
