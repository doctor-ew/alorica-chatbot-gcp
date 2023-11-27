import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import csv
import html
import re

# Updated cleaning function to handle complex HTML in meta tags
def clean_meta_content(content):
    # Parse with BeautifulSoup to extract text
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text(separator=' ')
    # Unescape HTML entities
    text = html.unescape(text)
    # Remove URLs, encoded characters, and excess whitespace
    text = re.sub(r'http\S+', '', text)  # Removes URLs
    text = re.sub(r'\s+', ' ', text)  # Reduces any whitespace to a single space
    return text.strip()  # Removes leading and trailing whitespace

def parse_xml_to_csv(xml_file, output_csv):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # Namespace handling
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    # Extract and clean URLs
    urls = [url.text.strip() for url in root.findall('.//ns:url/ns:loc', ns)]
    # Prepare to write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, escapechar='\\')
        # Write headers
        writer.writerow(['loc', 'description', 'description_clean'])
        for url in urls:
            try:
                # Clean up the URL, removing new lines and surrounding whitespace
                url = url.strip()
                print(f"|-U-| Processing {url}")
                # Fetch the content of the URL
                response = requests.get(url)
                response.raise_for_status()
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                # Find the meta description tag
                meta_tag = soup.find('meta', attrs={'name': 'description'})
                description = meta_tag['content'] if meta_tag else 'Description not found'
                # Clean the description using the updated function
                description_clean = clean_meta_content(description)
                print(f"|-D-| Description: {description_clean}")
                # Write row to CSV
                writer.writerow([url, description, description_clean])
            except Exception as e:
                print(f"Error processing {url}: {e}")

# Replace 'path_to_your_xml_file.xml' with the path to your XML file
parse_xml_to_csv('Alorica-sitemap.xml', 'output.csv')
