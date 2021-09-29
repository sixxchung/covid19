import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from settings.sixx    import *
dtf_cases = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", sep=",")

countrylist = ["World"] + dtf_cases["Country/Region"].unique().tolist()

group_by_country(dtf=dtf_cases, country)

# make table aaa
dtf = dtf.drop(['Province/State','Lat','Long'], axis=1)
dft = dtf.groupby("Country/Region").sum().T
dtf["World"] = dtf.sum(axis=1)

# filtering
dtf = dtf[country]
dtf.index = pd.to_datetime(dtf.index, infer_datetime_format=True)
ts =        pd.DataFrame(index=dtf.index, data=dtf.values, columns=["data"])
return ts