import requests


def get_country_info(country_name):
    api_key = ''
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': country_name,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    response = requests.get(service_url, params=params)
    data = response.json()
    return data

def get_neighboring_countries(country_code):
    username = ''
    api_url = f'http://api.geonames.org/neighboursJSON?country={country_code}&username={username}'
    response = requests.get(api_url)
    data = response.json()
    return data['geonames']

country_name = 'Poland'
country_info = get_country_info(country_name)

if 'itemListElement' in country_info:
    result = country_info['itemListElement'][0]
    country_name = result['result']['name']
    # country_code = result['result']['@id'].split(':')[3]
    print(f"Basic info about {country_name}:")
    print(f"Name: {country_name}")
    # print(f"Country code: {country_code}")

    country_code = "POL"
    neighboring_countries = get_neighboring_countries(country_code)
    print(f"\nNeighboring countries:")
    for neighbor in neighboring_countries:
        print(neighbor['countryName'])
else:
    print("No results found.")
