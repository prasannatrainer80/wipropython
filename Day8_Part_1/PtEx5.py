import pandas as pd
import numpy as np

df = pd.read_csv("d:/csv/Employ_Data_Dup.csv")
print(df)
df.sort_values("Name",inplace=True)
print(df)
duplicates=df[df.duplicated()]
print(duplicates)
duprem=df["Name"].duplicated(keep=False)
print(duprem)
df=df[~duprem]
print("------------removal----------------")
print(df)
df.info()