import numpy as np
import pandas as pd
from pandas import pivot

df = pd.read_csv("d:/csv/Indicator.csv")
output=df.pivot(index=['Country'], columns='Year',values='Value')
print(output)