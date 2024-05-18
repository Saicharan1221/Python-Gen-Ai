from api_integration.api_handler import fetch_data_from_api

from citation_identification.citation_identifier import identify_citations

# API Endpoint and Total Pages
base_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
total_pages = 34

# Fetch data from the API
api_data = fetch_data_from_api(base_url, total_pages)

# Identify citations
citations = identify_citations(api_data)

# Print the citations or pass them to the user interface for display
print(citations)
