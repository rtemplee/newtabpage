import dash
from dash import Dash, html, dcc, Input, Output, State, no_update

app = Dash(__name__, update_title='', suppress_callback_exceptions=True)

app.layout = html.Div(children=[
    html.Div('0', id='counter'),
    html.Button('Session Counter', id='fart'),
    html.Div('0', id='hidden-counter-div'),
    html.Button('Hidden Div Counter', id='sbd'),
    dcc.Store(id='session', storage_type='session')
])

@app.callback(
    Output('counter', 'children'),
    Output('session', 'data'),
    Input('fart', 'n_clicks'),
    State('session', 'data'),
)
def count(_, session_value):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'fart' in changed_id:
        if session_value == None:
            return 1, 1
        else:
            counter = int(session_value)
            counter += 1
            return counter, counter
    else:
        return session_value, session_value


if __name__ == "__main__":
    app.run_server(port='8050', debug=True)
