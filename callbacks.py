from dash.dependencies import Input, Output, State

from app import app

from layouts import DIRECTORY

@app.callback(
    [Output(f"{x}", "active") for x in DIRECTORY],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return ["Home" == x for x in DIRECTORY]
    return [pathname == f"/{x}" for x in DIRECTORY]

    #active turns off after clicking elsewhere on the page

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)

def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open
