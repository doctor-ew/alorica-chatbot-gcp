# local_test.py
import chatbot_core

test_request = {
    "queryResult": {
        "queryText": "Hello World"
    }
}

response = chatbot_core.process_chatbot_request(test_request)
print(response)
