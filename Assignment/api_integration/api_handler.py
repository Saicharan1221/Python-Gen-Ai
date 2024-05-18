import requests
import json

def fetch_data_from_api(base_url, total_pages):
    data_list = []
    for page_num in range(1, total_pages + 1):
        url = f"{base_url}?page={page_num}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Assuming the API response is a list of dictionaries
            if isinstance(data, list):
                data_list.extend(data)
            else:
                print("Invalid API response format. Expected a list of dictionaries.")
        else:
            print(f"Failed to fetch data from page {page_num}")
    return data_list
