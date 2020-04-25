import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from app import app
from layouts import home_page, navbar, page_not_found
import callbacks

from layouts import DIRECTORY

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return DIRECTORY['Home']
    elif f"{pathname}"[1:] in DIRECTORY:
        return DIRECTORY[ f"{pathname}"[1:]]
    else:
        return page_not_found(pathname)

if __name__ == '__main__':
    app.run_server(debug=True)