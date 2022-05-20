import os
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output


CORRELATION_DATA_DIR = 'data/correlation'
dropdown_corr_columns = []
for file in os.listdir(CORRELATION_DATA_DIR):
    column = file.split('_', 1)[0]
    dropdown_corr_columns.append(column)


data_geo = pd.read_csv('data/geo_position.csv')
unique_towns = sorted(data_geo['CITY'].unique())

app = Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(dropdown_corr_columns, dropdown_corr_columns[0], id='dropdown-col'),
    dcc.Dropdown(unique_towns, unique_towns[0], id='dropdown-town'),
    html.Div(id='free-space'),
    html.Div(id='dd-output-container')
])

@app.callback(
    Output('dd-output-container', 'children'),
    [Input('dropdown-col', 'value'),
    Input('dropdown-town', 'value')]
)
def update_output(col_value, town_value):
    # return f'Selected {value}'
    corr_matr = np.load(f'data/correlation/{col_value}_correlation_data.npy')
    index = unique_towns.index(town_value)
    data_geo['VALUES'] = corr_matr[index, :]
    px.set_mapbox_access_token(open(".mapbox_token").read())
    
    fig = px.scatter_mapbox(
        data_geo,
        size = [2] * len(data_geo.index), 
        lat="LAT", 
        lon="LNG", 
        color="VALUES",
        hover_name="CITY",
        color_continuous_scale=px.colors.cyclical.Phase,
    )
    
    fig.update_layout(
        height = 700,
        margin = {
            'l':5,
            'r':5,
            't':5,
            'b':5,
        },
        autosize=True,
        mapbox = {
            'style': "open-street-map",
            'zoom': 7.5
        }
    )
    fig.show()

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)