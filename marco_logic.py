import json
import os

DB_FILE = "marco_db.json"

def load_data():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except:
            return create_default_data()
    else:
        return create_default_data()

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def create_default_data():
    # HERE is where we name your spots!
    return {
        "spots": {
            "Driveway Left": "Free",
            "Driveway Right": "Free",
            "Street": "Free",
            "Side Lot": "Free",
            "Garage": "Free"
        }
    }

def reset_db():
    """Forces the database to restart with the new default spots"""
    data = create_default_data()
    save_data(data)
    return data

 
