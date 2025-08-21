import os
import sys
import csv
from src.exception import CustomException

def save_to_csv(file_path, data, headers=None):
    """Save a single row of data to CSV."""
    try:
        file_exists = os.path.isfile(file_path)

        with open(file_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if headers and not file_exists:
                writer.writerow(headers)

            writer.writerow(data)

    except Exception as e:
        raise CustomException(e, sys)


def is_duplicate(file_path, value, column_index=0):
    """Check if a value already exists in a specific column of CSV."""
    try:
        if not os.path.isfile(file_path):
            return False

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            return any(row[column_index] == value for row in reader)

    except Exception as e:
        raise CustomException(e, sys)
