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


def get_graph_with_bordering_countries(country, response):

    G = nx.Graph()
    G.add_node(country, size=150)  # Zmniejszony rozmiar dwukrotnie dla głównego kraju
    for neighbor in response:
        neighbor_name = neighbor['countryName']
        G.add_edge(country, neighbor_name)
        G.add_node(neighbor_name, size=100)  # Zmniejszony rozmiar dwukrotnie dla krajów sąsiednich

    pos = nx.spring_layout(G)  # układ wierzchołków
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    text_labels = []
    for node in pos:
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text_labels.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=text_labels,
        textposition='middle center',
        marker=dict(
            showscale=False,
            colorscale='Blues',
            size=[G.nodes[node]['size'] for node in G.nodes],
            color=['#ADD8E6' if node == country else '#D3D3D3' for node in G.nodes],  # Jasnoniebieski dla głównego kraju
            line_width=2,
            opacity=1))

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    # fig.show()
    graphJSON_02 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON_02