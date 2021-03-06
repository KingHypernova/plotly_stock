#https://plotly.com/python/getting-started/
# ADDITIONS
# 1) Mess with different headings/paragraphs

import plotly.express as px
#import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df1 = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

#set fig to any px or go object
fig = px.bar(df1, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(id='woof', children='''Dash: A web application framework for Python.'''),
    html.H3(children='''This is an H3'''), # using headings H2,H3...etc dont require their own div
    html.Div(children='''woff yo woof man'''), # extra divs can be different paragraphs

    dcc.Graph(id='example-graph',figure=fig)
])

if __name__ == '__main__':
    app.run_server()