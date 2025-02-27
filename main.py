import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Ensure 'Script' column has no NaN values, replacing them with an empty string
    df['Script'] = df['Script'].fillna("")
    
    # Normalize 'completed' column to boolean values
    df['completed'] = df['completed'].astype(str).str.lower().map(lambda x: True if x == 'true' else False)
    
    # Convert to the required JSON structure
    json_data = {
        "reels": df.apply(lambda row: {
            "title": row["title"],
            "script": f"Script: {row['Script']}",
            "category": row["category"],
            "completed": row["completed"]
        }, axis=1).tolist()
    }
    
    # Save to a JSON file
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)
    
    print(f"JSON file saved as {json_file}")

# Example usage
csv_file_path = "input.csv"  # Replace with actual CSV file path
json_file_path = "reels.json"  # Output JSON file name
csv_to_json(csv_file_path, json_file_path)
