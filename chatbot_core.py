# chatbot_core.py
import json
import openai
from openai import OpenAI
from google.cloud import secretmanager

def process_chatbot_request(request_data):
    # Parse JSON if input is a string
    if isinstance(request_data, str):
        request_data = json.loads(request_data)

    # Extract user input
    user_input = request_data['queryResult']['queryText']

    # Fetch API key and create OpenAI client
    secret_client = secretmanager.SecretManagerServiceClient()
    secret_name = "projects/980523551273/secrets/open-ai-key-for-alorica/versions/latest"
    response = secret_client.access_secret_version(name=secret_name)
    openai_api_key = response.payload.data.decode("UTF-8")
    client = OpenAI(api_key=openai_api_key)

    # Call OpenAI API
    openai_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    # Extract response content
    response_content = openai_response.choices[0].message.content

    # Prepare Dialogflow response
    return {"fulfillmentText": response_content}
