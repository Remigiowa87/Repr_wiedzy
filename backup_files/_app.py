import requests


def get_entity_info(query):
    api_key = ''
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    response = requests.get(service_url, params=params)
    data = response.json()
    return data

query = 'Poland'
response = get_entity_info(query)
print(response)
if 'itemListElement' in response:
    result = response['itemListElement'][0]
    description = result['result']['description']
    print(f"Description of {query}: {description}")
else:
    print("No results found.")
