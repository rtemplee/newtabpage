import os
import json
import sys
sys.dont_write_bytecode = True # No pychache

from dash import Dash
import assets.layouts as layouts

app = Dash(__name__, 
           update_title='',
           suppress_callback_exceptions=True) # For debugging

app.layout = layouts.hello_world

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port="8050", 
                   debug=True)
    

