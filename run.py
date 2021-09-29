# from FOLDER.FILE import CLASS
# from FOLDER.FILE import CONSTANT
# from FOLDER      import FILE
from settings.sixx    import *
from apps.dash import app
from settings         import config

app.run_server(
    debug = True,#config.debug, 
    host  = config.host, 
    port  = config.port
)