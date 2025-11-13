# csv_validator.py
import csv
def validate_headers(file_path, expected_headers):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        return headers == expected_headers
