def excel_to_json(file_path):
    # Read the Excel file
    data = pd.read_excel(file_path)
    # Convert the data to JSON format
    json_data = data.to_json(orient='records')
    return json_data
# Example usage
file_path = './media/rest.xlsx'
json_data = excel_to_json(file_path)

# Write JSON data to a file
with open('bobby.json', 'w') as f:
    f.write(json_data)

print("JSON data has been stored in 'bobby.json'")

import json

# Read the JSON file
with open('bobby.json', 'r') as f:
    json_data = json.load(f)

# Function to count null values and replace them with float values from 1.0 to 10.0
def clean_json(json_data):
    num_null_values = 0
    for record in json_data:
        for key, value in record.items():
            if value is None:
                num_null_values += 1
                # Replace null value with float values from 1.0 to 10.0
                record[key] = float(num_null_values % 10 + 1)
    return num_null_values

# Clean the JSON data
null_count = clean_json(json_data)

# Write the cleaned JSON data back to the file
with open('bobby_cleaned.json', 'w') as f:
    json.dump(json_data, f, indent=4)

print(f"Number of null values replaced: {null_count}")
print("Cleaned JSON data has been stored in 'bobby_cleaned.json'")

import pandas as pd
import json

# Read the cleaned JSON file
with open('bobby_cleaned.json', 'r') as f:
    cleaned_json_data = json.load(f)

# Convert the JSON data to a DataFrame
df = pd.DataFrame(cleaned_json_data)

# Write the DataFrame to a CSV file
df.to_csv('bobby_cleaned.csv', index=False)

print("Cleaned JSON data has been converted to 'bobby_cleaned.csv'")
