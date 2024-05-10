import json
import warnings

import geopandas as gpd
import networkx as nx
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go
import requests
from flask import Flask, render_template, request, url_for

from geonames import get_country_code, get_country_population, get_neighboring_countries
from google_graph import get_google_graph_api_data
from img_plotly.graph import get_graph_with_bordering_countries
from img_plotly.world import get_world_map

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html') 
    else:
        if 'country' in request.form:
            country = request.form['country']


        # I img -WOLRD
        graphJSON_01 = get_world_map(country)

        # II img -GRAPH
        country_code = get_country_code(country)
        response = get_neighboring_countries(country_code)
        graphJSON_02 = get_graph_with_bordering_countries(country,response)

        population = get_country_population(country)
        population = '{:,.2f} million'.format(population / 10**6)


        return render_template('graph.html', graphJSON_01=graphJSON_01,
                                             graphJSON_02=graphJSON_02,
                                             country=country,
                                             population = population)


@app.route('/graph')
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City', 
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('graph.html', graphJSON=graphJSON)


if __name__ =='__main__':
    app.run()