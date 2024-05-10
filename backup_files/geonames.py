import requests


def get_country_code(country):
    username = 'magdast'
    api_url = f'http://api.geonames.org/searchJSON?q={country}&username={username}'
    response = requests.get(api_url)
    data = response.json()
    # print(data)
    return data['geonames'][0]['countryCode']



def get_neighboring_countries(country_code):
    username = 'magdast'
    api_url = f'http://api.geonames.org/neighboursJSON?country={country_code}&username={username}'
    response = requests.get(api_url)
    data = response.json()
    print(data)
    return data['geonames']



# country = "Italy"
# country_code = get_country_code(country)
# print('country_code:', country_code)
# response = get_neighboring_countries(country_code)
# print(response)

# for item in response:
#     print(item[0]['capital'])
#     # print(item[0])


# for neighbor in response:
#     print(neighbor['countryName'])


import requests


def get_country_population(country):
    username = 'magdast'
    api_url = f'http://api.geonames.org/searchJSON?q={country}&username={username}&type=json&featureCode=PCLI'
    response = requests.get(api_url)
    data = response.json()
    if 'geonames' in data and data['geonames']:
        for entry in data['geonames']:
            if entry['name'].lower() == country.lower():
                country_population = entry['population']
                return country_population
        

# Example usage:
country = "Italy"
population = get_country_population(country)











