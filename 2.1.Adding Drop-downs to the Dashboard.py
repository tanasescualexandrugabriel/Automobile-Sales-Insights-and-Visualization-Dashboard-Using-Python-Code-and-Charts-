import dash
from dash import dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout with a title and drop-down
app.layout = html.Div(children=[
    html.H1(children='Automobile Sales and Economic Impact Analysis Dashboard'),

    # Drop-down for selecting vehicle type
    html.Label('Select Vehicle Type'),
    dcc.Dropdown(
        id='vehicle-type-dropdown',
        options=[
            {'label': 'Sedan', 'value': 'SEDAN'},
            {'label': 'SUV', 'value': 'SUV'},
            {'label': 'Truck', 'value': 'TRUCK'}
        ],
        value='SEDAN'  # Default value
    ),

    # Placeholder for a graph (to be populated later)
    dcc.Graph(id='example-graph')
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
