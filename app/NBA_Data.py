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

