import pandas as pd
import string

def clean_description(description):
    """
    Function to clean the description field.
    - Converts to lowercase
    - Removes punctuation
    - Strips extra whitespaces
    """
    # Convert to lowercase
    clean_desc = description.lower()

    # Remove punctuation
    clean_desc = clean_desc.translate(str.maketrans('', '', string.punctuation))

    # Strip extra whitespaces
    clean_desc = " ".join(clean_desc.split())

    return clean_desc

# Load the original CSV file
original_file_path = 'Alorica_sitemap_orig.csv'  # Replace with your file path
original_df = pd.read_csv(original_file_path)

# Apply the cleaning function to the description column
original_df['description_clean'] = original_df['description'].apply(clean_description)

# Save the resulting dataframe to a new CSV file
output_file_path = 'cleaned_Alorica_sitemap_orig.csv'  # Replace with your desired output path
original_df.to_csv(output_file_path, index=False)

# Print message on completion
print(f"File cleaned and saved to {output_file_path}")
