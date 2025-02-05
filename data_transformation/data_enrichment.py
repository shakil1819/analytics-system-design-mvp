import requests

class DataEnrichment:
    def __init__(self, data):
        self.data = data

    def enrich_data(self, api_url, api_key):
        enriched_data = []
        for record in self.data:
            response = requests.get(api_url, headers={'Authorization': f'Bearer {api_key}'}, params={'query': record})
            if response.status_code == 200:
                enriched_record = response.json()
                enriched_data.append(enriched_record)
            else:
                enriched_data.append(record)
        return enriched_data

    def fact_check_data(self, fact_checking_service_url, api_key):
        fact_checked_data = []
        for record in self.data:
            response = requests.get(fact_checking_service_url, headers={'Authorization': f'Bearer {api_key}'}, params={'query': record})
            if response.status_code == 200:
                fact_checked_record = response.json()
                fact_checked_data.append(fact_checked_record)
            else:
                fact_checked_data.append(record)
        return fact_checked_data

# Example usage
if __name__ == "__main__":
    # Sample data
    data = ["example data 1", "example data 2"]

    enricher = DataEnrichment(data)
    enriched_data = enricher.enrich_data("https://api.example.com/enrich", "your_api_key")
    fact_checked_data = enricher.fact_check_data("https://api.example.com/fact-check", "your_api_key")

    print("Enriched data:\n", enriched_data)
    print("Fact-checked data:\n", fact_checked_data)
