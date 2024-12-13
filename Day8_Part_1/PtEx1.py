import pandas as pd
import numpy as np

df = pd.read_csv("d:/csv/Data.csv")
print(df)

pivot_df = df.pivot_table(index='Qualification',columns='Name',values='Age')
print(pivot_df)
result = df.pivot_table(index='Name',columns='Qualification',values='Age')

print('-----------------------')
print(result)