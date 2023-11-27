import re
import csv
from bs4 import BeautifulSoup
import html

def clean_meta_content(content):
    # Use BeautifulSoup to remove HTML tags
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text(separator=' ')
    # Unescape HTML entities
    text = html.unescape(text)
    # Remove any residual HTML tags that may have been missed
    text = re.sub(r'<[^>]+>', '', text)
    # Remove commas, URLs, encoded characters, and excess whitespace
    text = re.sub(r',', '', text)  # Remove commas
    text = re.sub(r'http\S+', '', text)  # Removes URLs
    text = re.sub(r'\s+', ' ', text).strip()  # Reduces any whitespace to a single space
    return text

def clean_csv(input_file, output_file):
    # Read the input CSV and clean up the rows
    with open(input_file, 'r', encoding='utf-8-sig') as infile, open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        # Write the header to the output CSV
        headers = next(reader)
        writer.writerow(['loc', 'description'])  # New header without 'description_clean'

        for row in reader:
            loc = row[0].replace('"', '').replace('\n', ' ').replace('\r', ' ').strip()
            # Clean the 'description_clean' using the updated function and rename it to 'description'
            description = clean_meta_content(row[2])  # Assuming 'description_clean' is the third column

            writer.writerow([loc, description])

# Specify the input and output file names
input_csv = 'output.csv'  # This should be the file path to your original output CSV
output_csv = 'ChatGPT_Alorica_Sitemap.csv'  # The new file to be saved

clean_csv(input_csv, output_csv)
