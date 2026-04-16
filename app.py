from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from utils.data_loader import load_data
from components.map import create_map
from components.filters import create_filters

# Initialize app
app = Dash(__name__)

# Load data
df = load_data()

# Layout
app.layout = html.Div([
    
    html.H1("Terrorism Analysis Dashboard"),
    
    # Filters
    create_filters(df),
    
    # Map
    dcc.Graph(id='map')
])

# Callback (Dropdown → Map)
@app.callback(
    Output('map', 'figure'),
    Input('country', 'value')
)
def update_map(selected_country):
    
    if selected_country:
        filtered_df = df[df['country_txt'] == selected_country]
    else:
        filtered_df = df

    return create_map(filtered_df)


# Run app
if __name__ == "__main__":
    app.run(debug=True)