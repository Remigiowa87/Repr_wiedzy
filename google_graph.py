import requests


def get_google_graph_api_data(query):
    api_key = open('.api_key').read()
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }

    response  = requests.get(service_url, params=params)
    data = response.json()
    return data



# query = 'Poland'
# response = get_google_graph_api_data(query)
# print(response)

# if 'itemListElement' in response:
#     for element in response['itemListElement']:
#         print(element['result']['name'])

