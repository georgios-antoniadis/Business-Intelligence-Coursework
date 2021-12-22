import numpy as np
import pandas as pd
import json
from pandas_profiling import ProfileReport

data = json.load(open('../allData/1987q1.json'))

df = pd.json_normalize(data['results'])

print(df.info())

df.to_csv (r'test.csv', index = None)

cs = pd.read_csv("test.csv")


profile = ProfileReport(cs, title="Pandas Profiling Report")

profile.to_file("your_report2.html")