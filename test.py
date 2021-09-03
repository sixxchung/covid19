import pandas as pd

dtf_cases = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", sep=",")
type(dtf_cases)
dtf_cases['Country/Region']

#countrylist = ["World"] + 


#cc=dtf_cases["Country/Region"].unique().tolist()

#["world"] + cc[0:3]