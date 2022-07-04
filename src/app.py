from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from pages.exploratory import page as exploratory_page
from pages.prediction import page as prediction_page
from pages.about_us import page as about_us_page
from pages.home import page as home_page
import main_layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,  dbc.icons.FONT_AWESOME], suppress_callback_exceptions=True)
app.title = "DS4a Crime Dashboard - Team 234"

server = app.server

app.layout = main_layout.layout

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/prediction':
        return prediction_page.layout
    if pathname == '/exploratory':
        return exploratory_page.layout
    if pathname == '/about-us':
        return about_us_page.layout
    else:
       return home_page.layout 

if __name__ == '__main__':
    app.run_server(debug=True)