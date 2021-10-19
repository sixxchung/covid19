import os
## App settings
name = ""
host = "localhost" # "0.0.0.0"
port = int(os.environ.get("PORT", 5555))

#debug = True #False
myBlog = "https://onesixx.com/dash-layout-bootstrap-components/"
baseBlog = "https://towardsdatascience.com/how-to-embed-bootstrap-css-js-in-your-python-dash-app-8d95fc9e599e"
code = "https://github.com/mdipietro09/App_VirusForecaster"
fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
#tutorial = "https://towardsdatascience.com/how-to-embed-bootstrap-css-js-in-your-python-dash-app-8d95fc9e599e"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


## File system
# __file__
# '/Users/onesixx/sixxDoc/PCODE/covid19/settings/config.py'
root = os.path.dirname(os.path.dirname(__file__)) + "/"

## DB
