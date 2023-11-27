import pandas as pd

def process_csv(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Extracting intents and responses
    intents_responses = {}
    for _, row in data.iterrows():
        # Here, the URL is used to create a unique intent name
        intent_name = row['loc'].split('/')[-1]  # Example: 'subscription-management'
        intents_responses[intent_name] = row['description_clean']

    return intents_responses

# Example usage
file_path = 'https://storage.cloud.google.com/alorica-sitemap/ChatGPT_Alorica_Sitemap.csv'
intents_responses = process_csv(file_path)
