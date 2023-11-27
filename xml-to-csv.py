import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import pandas as pd
import re

def clean_description(desc):
    # Convert to lowercase and remove special characters and commas
    return re.sub(r'[^a-zA-Z0-9\s]', '', desc.lower())

def parse_xml_to_csv(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace handling
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Extract URLs
    urls = [url.text for url in root.findall('.//ns:url/ns:loc', ns)]

    # Create a DataFrame
    df = pd.DataFrame(columns=['loc', 'description', 'description_clean'])

    for url in urls:
        try:
            # Fetch the content of the URL
            response = requests.get(url)
            response.raise_for_status()

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the meta description tag
            meta_tag = soup.find('meta', attrs={'name': 'description'})
            description = meta_tag['content'] if meta_tag else 'Description not found'

            print(f"|-o-| Processed {url} and found meta_tag {meta_tag} and description: {description}")
            # Clean the description
            description_clean = clean_description(description)
            print(f"|-o-| Cleaned description: {description_clean}")
            # Append to the DataFrame
            df.loc[len(df)] = [url, description, description_clean]

        except Exception as e:
            print(f"Error processing {url}: {e}")

    # Save to CSV
    df.to_csv('output.csv', index=False)

# Replace 'path_to_your_xml_file.xml' with the path to your XML file
parse_xml_to_csv('Alorica-sitemap.xml')
