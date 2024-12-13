import numpy as np
import pandas as pd
from pandas import pivot

df = pd.read_csv("d:/csv/Employs.csv")
output=df.pivot(index=['Dept'], columns='name',values='Salary')
print(output)