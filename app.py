from flask import Flask, render_template, request, url_for

from geonames import get_country_code, get_neighboring_countries
from google_graph import get_google_graph_api_data

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html') 
    else:
        if 'country' in request.form:
            country = request.form['country']


            # Data - work in progress

            # GOOGLE
            response = get_google_graph_api_data(country)
            # print(response)
            if 'itemListElement' in response:
                result = response['itemListElement'][0]
                description = result['result']['description']
                print(f"Description of {country}: {description}")
            else:
                print("No results found.")


            # GEONAME
            country_code = get_country_code(country)
            response = get_neighboring_countries(country_code)
            
            for neighbor in response:
                print(neighbor['countryName'])

                                    
            return render_template('index.html') 


if __name__ =='__main__':
    app.run()