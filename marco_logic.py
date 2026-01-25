import json
import os

# The file where we save parking data
DB_FILE = "marco_db.json"

def load_data():
    # If the file exists, load it. If not, return default empty spots.
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except:
            return create_default_data()
    else:
        return create_default_data()

def save_data(data):
    # Save the dictionary to the text file
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def create_default_data():
    return {
        "spots": {
            "1": "Free",
            "2": "Free",
            "3": "Free",
            "4": "Free"
        }
    }
