import pandas as pd

dtf_cases = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", sep=",")
type(dtf_cases)
dtf_cases['Country/Region']

#countrylist = ["World"] + 


#cc=dtf_cases["Country/Region"].unique().tolist()

#["world"] + cc[0:3]
# To print multiple output in a cell --------------------------
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# 클래스에서(인스턴스에서도) 직접 접근가능한 메소드 (정적메소드)는 
# 인스턴스method의 1st인자가 self
# classmethod의 1st인자는 클래스
# staticmethod 특별히 추가되는 인자없음

class myClass:
    var = "AAA" 
    def add_instance_method(self, a, b):
        return a+b

    @classmethod
    def add_class_method(cls, a, b):
        return a-b

    @staticmethod
    def add_static_method(a, b):
        return a*b

class childClass(myClass):
    var = "BBB"
