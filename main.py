import openai
from openai import OpenAI
import json
from google.cloud import secretmanager

def alorica_chatbot(request_json):
    # If the input is a string, parse it as JSON
    if isinstance(request_json, str):
        request_json = json.loads(request_json)

    # Assuming request_json is a dictionary with the right structure
    user_input = request_json['queryResult']['queryText']

    # Fetch the OpenAI API key from Secret Manager
    secret_client = secretmanager.SecretManagerServiceClient()
    secret_name = "projects/980523551273/secrets/open-ai-key-for-alorica/versions/latest"
    response = secret_client.access_secret_version(name=secret_name)
    openai_api_key = response.payload.data.decode("UTF-8")

    # Create an OpenAI client with the fetched API key
    client = OpenAI(api_key=openai_api_key)

    # Call OpenAI API using the updated method
    try:
        openai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Replace with gpt-4-turbo
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
    except openai.OpenAIError as e:
        return f"An error occurred: {str(e)}"


    print('|-o-| openai_response',openai_response)

    # Extracting the response content
    response_content = openai_response.choices[0].message.content  # Accessing the 'content' attribute  # Use 'text' instead of 'content'

    # Prepare the response for Dialogflow
    dialogflow_response = {
        "fulfillmentText": response_content,
    }

    return json.dumps(dialogflow_response)

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('DoctorEw')
    # Simulate a Dialogflow request JSON
    test_request = {
        "queryResult": {
            "queryText": "Hello World"
        }
    }
    print(alorica_chatbot(test_request))
