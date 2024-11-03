import dash
from dash import dcc, html, Output, Input
import plotly.express as px
import pandas as pd

# Sample data for different vehicle types
data = {
    'Vehicle Type': ['Sedan', 'SUV', 'Truck'],
    'Sales Volume': [85000, 62000, 45000],
    'Average Price': [25000, 32000, 45000]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout with drop-down and output container
app.layout = html.Div([
    html.H1("Automobile Sales Dashboard"),
    dcc.Dropdown(
        id='vehicle-type-dropdown',
        options=[{'label': vehicle, 'value': vehicle} for vehicle in df['Vehicle Type']],
        value='Sedan'
    ),
    dcc.Graph(id='output-graph')
])

# Callback to update the graph based on vehicle type selection
@app.callback(
    Output('output-graph', 'figure'),
    Input('vehicle-type-dropdown', 'value')
)
def update_graph(selected_vehicle):
    # Filter the data based on the selected vehicle type
    filtered_data = df[df['Vehicle Type'] == selected_vehicle]
    
    # Create a bar chart for the selected vehicle type
    fig = px.bar(
        filtered_data,
        x='Vehicle Type',
        y='Sales Volume',
        title=f'Sales Volume for {selected_vehicle}'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
