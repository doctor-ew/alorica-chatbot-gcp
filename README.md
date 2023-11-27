   # Alorica Chatbot for GCP

   ## Overview
   This repository contains a series of Python scripts and a Flask application designed to create a sophisticated chatbot for Alorica, utilizing Dialogflow on Google Cloud Platform (GCP). The chatbot is built to handle inquiries based on Alorica's website content, providing users with accurate and helpful responses.

   ### Components
   - `xml-to-csv.py`: Converts Alorica's website sitemap XML to a CSV file containing URLs and corresponding meta descriptions.
   - `csv_cleaner.py`: Cleans and preprocesses the CSV file for more efficient processing.
   - `csv_processor.py`: Processes the cleaned CSV file to extract relevant information for Dialogflow intents.
   - `intent_creator.py`: Creates intents in Dialogflow programmatically using the processed data, adding training phrases and responses.
   - `main.py`: Flask application deployed as a Google Cloud Function to handle chatbot interactions.

   ## Setup and Deployment
   ### Prerequisites
   - Google Cloud Platform account
   - Access to Dialogflow and Cloud Functions
   - Python 3.x

   ### Installation
   1. Clone the repository.
   2. Install required dependencies: `pip install -r requirements.txt`

   ### Configuration
   - Set up Google Cloud credentials and provide necessary permissions for Dialogflow API and Cloud Storage.
   - Update the project ID and other configurations in the scripts as required.

   ### Running the Scripts
   - Execute `xml-to-csv.py` to generate the initial CSV from the XML sitemap.
   - Run `csv_cleaner.py` to preprocess the CSV file.
   - Use `csv_processor.py` to prepare data for Dialogflow.
   - `intent_creator.py` can be run to create/update intents in Dialogflow.

   ### Deploying the Chatbot
   - Deploy `main.py` as a Google Cloud Function.
   - Ensure the Dialogflow agent is correctly linked and configured.

   ## Usage
   After deployment, the chatbot can be interacted with through the configured interfaces (e.g., Alorica's website, integration platforms).

   ## Contributing
   Contributions to this project are welcome. Please follow standard GitHub procedures for forking the repository, making changes, and submitting pull requests.