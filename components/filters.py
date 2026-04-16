from dash import dcc, html

def create_filters(df):
    return html.Div([
        dcc.Dropdown(
            id='country',
            options=[{'label': i, 'value': i} for i in df['country_txt'].unique()],
            placeholder="Select Country"
        )
    ])