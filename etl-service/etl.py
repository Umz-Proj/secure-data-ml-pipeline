import requests
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://jsonplaceholder.typicode.com/posts"


def extract_data():
    try:
        logging.info("Starting data extraction from API")
        response = requests.get(API_URL, timeout=10)

        # Check if request succeeded
        if response.status_code != 200:
            logging.error(f"Failed API call. Status code: {response.status_code}")
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None


def transform_data(data):
    if not isinstance(data, list):
        logging.warning("Unexpected data format received")
        return None

    # Only keep selected fields
    transformed = [
        {
            "id": item.get("id"),
            "title": item.get("title")
        }
        for item in data
        if "id" in item and "title" in item
    ]

    logging.info(f"Transformed {len(transformed)} records")
    return transformed


def load_data(data):
    if not data:
        logging.warning("No data to load")
        return

    filename = f"processed_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"Data successfully saved to {filename}")


def main():
    raw_data = extract_data()
    if raw_data:
        clean_data = transform_data(raw_data)
        load_data(clean_data)


if __name__ == "__main__":
    main()
    print("ETL pipeline executed successfully inside Docker.")