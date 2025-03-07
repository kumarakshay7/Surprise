import csv
import os
import json

DATA_FILE = "user_data.csv"

def initialize_data_file():
    """Create the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score", "Answers"])

def store_user_data(name, score, answers):
    """
    Store the user's name, score, and answers in the CSV file.
    The answers dictionary is saved as a JSON string.
    """
    initialize_data_file()
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score, json.dumps(answers)])
