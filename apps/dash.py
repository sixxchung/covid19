import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
###############################################################################
#                                MAIN                                         #
###############################################################################
import dash
import dash_bootstrap_components as dbc
import dash_core_components      as dcc
import dash_html_components      as html

import dash_admin_components as dac

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from apps.uimodule.cards        import cards_tab
from apps.uimodule.social_cards import social_cards_tab
from apps.uimodule.tab_cards    import tab_cards_tab
from apps.uimodule.basic_boxes  import basic_boxes_tab
from apps.uimodule.value_boxes  import value_boxes_tab
from apps.uimodule.tab_cards    import text_1, text_2, text_3
from apps.uimodule.example_plots  import plot_scatter

from pycode.data   import MyData
from pycode.model  import MyModel
from pycode.result import MyResult

from settings      import config, contents, style
#from settings      import sixx, config, contents, style

# Read data
myData = MyData()
myData.get_data()   # data.dtf_cases, data.countrylist

# =============================================================================
# Dash App and Flask Server
# =============================================================================
# App Instance
app = dash.Dash(
    name = config.name, 
    assets_folder = config.root+"/apps/assets", 
    external_stylesheets = [
        dbc.themes.SLATE, 
        config.fontawesome,
        config.external_stylesheets,
    ]
)
server = app.server 

app.title = config.name
# dash.Dash( 
#     name=None, server=True, eager_loading=False,
#     assets_folder="assets", assets_url_path="assets", assets_ignore="", assets_external_path=None, include_assets_files=True, 
#     url_base_pathname=None, requests_pathname_prefix=None, routes_pathname_prefix=None, 
#     serve_locally=True, compress=None, meta_tags=None, 
#     index_string=_default_index,
#     external_scripts=None, external_stylesheets=None, 
#     suppress_callback_exceptions=None, 
#     prevent_initial_callbacks=False, 
#     show_undo_redo=False, extra_hot_reload_paths=None, 
#     plugins=None, title="Dash", update_title="Updating...", 
#     **obsolete
# )

### Navbar
# right_ui = dac.NavbarDropdown(
# 	badge_label = "!",
#     badge_color= "danger",
#     src = "https://quantee.ai",
# 	header_text="2 Items",
#     children= [
# 		dac.NavbarDropdownItem(
# 			children = "message 1",
# 			date = "today"
# 		),
# 		dac.NavbarDropdownItem(
# 			children = "message 2",
# 			date = "yesterday"
# 		),
# 	]
# )
# dbc.Nav([
#     dbc.NavItem(),
#     dbc.NavItem(),
#     dbc.DropdownMenu()
# ])


navbar = dbc.Navbar(
    className="nav nav-pills", 
    color="dark",
    dark=True,
    #text="I can write text in the navbar!",
    children=[
        dbc.NavItem( ## logo/home
            html.Img(src=app.get_asset_url("logo_covid19.jpg"), height="40px")
        ),
        dbc.NavItem( ## about
            html.Div([
                dbc.NavLink("About", id="about-popover", href="/", active=False),
                dbc.Popover(id="about", is_open=False, target="about-popover", 
                    children=[
                        dbc.PopoverHeader("How it works"), 
                        dbc.PopoverBody(contents.txt_about)
                    ]
                )
            ])
        ),
        dbc.DropdownMenu( ## links
            label="Links", nav=True, 
            children=[
                dbc.DropdownMenuItem([html.I(className="fa fa-"), "my Blog"], href=config.myBlog, target="_blank"), 
                dbc.DropdownMenuItem([html.I(className="fa fa-github"),   "  Tutorial"], href=config.baseBlog, target="_blank"),
                dbc.DropdownMenuItem([html.I(className="fa fa-github"),   "  Code"], href=config.code, target="_blank")
            ]
        )
    ]
)


# Input
inputs = dbc.FormGroup([
    html.H5("Select Country"),
    dcc.Dropdown( id="country", 
        options=[{"label":x, "value":x} for x in myData.countrylist], 
        value="World"
    )
])
sidebar= html.Div(
    [
        html.H2('Parameters', style=style.TEXT),
        html.Hr(),
        #controls
    ],
    style=style.SIDEBAR,
)

analyBody = dbc.Row([
    ### input + panel
    dbc.Col(md=2, children=[
        inputs, 
        html.Br(),html.Br(),html.Br(),
        html.Div(id="output-panel")
    ]),
    ### plots
    dbc.Col(md=9, children=[
        dbc.Col(html.H4("Forecast 30 days from today"), width={"size":4,"offset":8}), 
        #dbc.Tabs([
        #    dbc.Tab(dcc.Graph(id="plot-total"),  label="Total cases"),
        #    dbc.Tab(dcc.Graph(id="plot-active"), label="Active cases")
        #])
        dbc.Tabs(className="nav nav-pills", children=[
            dbc.Tab(
                dcc.Graph(id="plot-total"),  label="Total cases"),
            dbc.Tab(
                dcc.Graph(id="plot-active"), label="Active cases")
        ])
    ])
])

# App Layout
app.layout = dbc.Container(fluid=True, children=[
    ## Top
    html.H1(config.name, id="nav-pills"),
    navbar,
    html.Br(),#html.Br(),html.Br(),
    ## Body
    dbc.Row([
        html.Div([sidebar, analyBody])
        # ### input + panel
        # dbc.Col(md=2, children=[
        #     sidebar
        # ]),
        # ### plots
        # dbc.Col(md=9, children=[
        # analyBody
        # ])
    ])
])

###  navitem-popover
@app.callback(
    output =  Output("about",       "is_open"), 
    inputs = [Input("about-popover","n_clicks")], 
    state  = [State("about",        "is_open")] )
def about_popover(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    output =  Output("about-popover", "active"), 
    inputs = [Input("about-popover", "n_clicks")], 
    state  = [State("about-popover", "active")] )
def about_active(n, active):
    if n:
        return not active
    return active

### plot total cases
@app.callback(
    output = Output("plot-total", "figure"), 
    inputs = [Input("country", "value")] ) 
def plot_total_cases(country):
    print(country)
    myData.process_data(country) 
    # myData.dtf
    model = MyModel(myData.dtf)
    model.forecast()
    #model.add_deaths(data.mortality)
    # model.dtf
    result = MyResult(model.dtf)
    return result.plot_total(model.today)

'''     
#  plot active cases
@app.callback(
    output= Output("plot-active","figure"), 
    inputs=[Input("country","value")] )
def plot_active_cases(country):
    data.process_data(country) 
    model = Model(data.dtf)
    model.forecast()
    #model.add_deaths(data.mortality)
    result = Result(model.dtf)
    return result.plot_active(model.today)
    
# render output panel
@app.callback(
    output= Output("output-panel","children"), 
    inputs=[Input("country","value")] )
def render_output_panel(country):
    data.process_data(country) 
    model = Model(data.dtf)
    model.forecast()
    #model.add_deaths(data.mortality)
    result = Result(model.dtf)
    peak_day, num_max, total_cases_until_today, total_cases_in_30days, active_cases_today, active_cases_in_30days = result.get_panel()
    peak_color = "white" if model.today > peak_day else "red"
    panel = html.Div([
        html.H4(country),
        dbc.Card(body=True, className="text-white bg-primary", children=[
            html.H6("Total cases until today:", style={"color":"white"}),
            html.H3("{:,.0f}".format(total_cases_until_today), style={"color":"white"}),
            
            html.H6("Total cases in 30 days:", className="text-danger"),
            html.H3("{:,.0f}".format(total_cases_in_30days), className="text-danger"),
            
            html.H6("Active cases today:", style={"color":"white"}),
            html.H3("{:,.0f}".format(active_cases_today), style={"color":"white"}),
            
            html.H6("Active cases in 30 days:", className="text-danger"),
            html.H3("{:,.0f}".format(active_cases_in_30days), className="text-danger"),
            
            html.H6("Peak day:", style={"color":peak_color}),
            html.H3(peak_day.strftime("%Y-%m-%d"), style={"color":peak_color}),
            html.H6("with {:,.0f} cases".format(num_max), style={"color":peak_color})
        
        ])
    ])
    return panel
'''