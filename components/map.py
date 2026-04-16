import plotly.express as px

def create_map(df):
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        hover_name='country_txt',
        title='Terrorism Map'
    )
    return fig