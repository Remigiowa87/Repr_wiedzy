import requests


def get_country_code(country):
    username = open('.GeoNames_Username').read()
    api_url = f'http://api.geonames.org/searchJSON?q={country}&username={username}'
    response = requests.get(api_url)
    data = response.json()
    return data['geonames'][0]['countryCode']



def get_neighboring_countries(country_code):
    username = open('.Geonames_Username').read()
    api_url = f'http://api.geonames.org/neighboursJSON?country={country_code}&username={username}'
    response = requests.get(api_url)
    data = response.json()
    return data['geonames']



def get_country_population(country):
    username = open('.Geonames_Username').read()
    api_url = f'http://api.geonames.org/searchJSON?q={country}&username={username}&type=json&featureCode=PCLI'
    response = requests.get(api_url)
    data = response.json()
    if 'geonames' in data and data['geonames']:
        for entry in data['geonames']:
            if entry['name'].lower() == country.lower():
                country_population = entry['population']
                return country_population
        



# country = "Italy"
# country_code = get_country_code(country)
# print('country_code:', country_code)
# response = get_neighboring_countries(country_code)
# # print(response)

# for neighbor in response:
#     print(neighbor['countryName'])
