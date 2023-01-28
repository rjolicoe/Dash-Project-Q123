from dash import Dash, dash_table, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import Data.NBA_API as NBA
from dash_bootstrap_components._components.Container import Container
import sqlite3

NBAR = NBA.NBA_Data_Retrieval()
NBA_DF = NBAR.retrieve_data()

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

nba_df = dash_table.DataTable(NBA_DF.to_dict('records'),
                              [{"name": i, "id": i} for i in NBA_DF.columns])

#set the app.layout
app.layout = \
    navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Additional Details", href="#", id='Nav')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True, id="Test"),
                dbc.DropdownMenuItem("NBA Players", href="#",
                                     id = 'nba'),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NBA Player Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

# @app.callback(Output('tabs-content', 'children'),
#               [Input('tabs', 'value')])
# def render_content(tab):
#     if tab == 'tab-1':
#         return nba_df
#     elif tab == 'tab-2':
#         return html.H1('Tab 2')

if __name__ == '__main__':
    app.run(debug=True)