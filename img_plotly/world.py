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

warnings.filterwarnings("ignore")
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# Mapa świata
world_map = go.Figure()

# Dodania granić
for country in world['name']:
    country_data = world[world['name'] == country]
    world_map.add_trace(go.Scattergeo(
        lon=country_data.centroid.x,
        lat=country_data.centroid.y,
        text=country_data['name'],
        mode='markers',
        marker=dict(size=10, color='red'),
        name=country
    ))


# Aktualizujemy layout mapy
world_map.update_layout(
    title_text='Mapa świata',
    geo=dict(
        showcoastlines=True,
        projection=dict(type="natural earth")  # ustawiamy typ projekcji na "natural earth"
    ),
    margin=dict(l=0, r=0, t=0, b=0)  # usuwamy marginesy
)
 


def get_world_map(country_name):
    world_map.data = []

    country_data = world[world['name'].str.lower() == country_name.lower()]
    if not country_data.empty:
        world_map.add_trace(go.Scattergeo(
        lon=country_data.centroid.x,
        lat=country_data.centroid.y,
        mode='markers',
        marker=dict(size=10, color='blue'),
        name=country_name  # Wyświetlamy nazwę wybranego kraju po prawej stronie mapy
    ))
        
        

    fig = world_map
    fig.update_layout(width=700, height=500)
    # fig.update_layout(width=1200, height=1000)
    graphJSON_01 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON_01