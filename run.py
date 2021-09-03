# from folder.file import constant
# from folder      import file
from application.dash import app
from settings         import config

app.run_server(
    debug = True,#config.debug, 
    host  = config.host, 
    port  = config.port
)