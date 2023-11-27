from google.cloud import storage
import pandas as pd
from io import StringIO

def download_blob_to_dataframe(bucket_name, source_blob_name):
    """Downloads a blob from the bucket and loads it into a DataFrame."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    # Download the contents of the blob as a string and then convert it to a DataFrame
    data = blob.download_as_text()
    return pd.read_csv(StringIO(data))

def process_csv(bucket_name, blob_name):
    # Load the CSV file from GCS
    data = download_blob_to_dataframe(bucket_name, blob_name)

    # Extracting intents and responses
    intents_responses = {}
    for _, row in data.iterrows():
        print("|-o-| Processing row", row)
        if 'loc' in data.columns:
            intent_name = row['loc'].split('/')[-1]  # Example: 'subscription-management'
            intents_responses[intent_name] = row['description']
        else:
            print("Column 'loc' not found in CSV.")

    return intents_responses

# Example usage
bucket_name = 'alorica-sitemap'
blob_name = 'ChatGPT_Alorica_Sitemap.csv'
intents_responses = process_csv(bucket_name, blob_name)
