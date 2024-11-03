import dash
from dash import dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout with a meaningful title
app.layout = html.Div(children=[
    html.H1(children='Automobile Sales and Economic Impact Analysis Dashboard'),
    dcc.Graph(id='example-graph'),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
