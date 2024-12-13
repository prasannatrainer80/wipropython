import pandas as pd
import numpy as np
df = pd.read_csv("d:/csv/Employ_Data.csv")
print(df)
print('---------------------------------------------------')
table1=df.pivot(index=['Dept'], columns='Name',values='Salary')
print(table1)
print("----------------------------------------------")
table2=df.pivot(index=['Name'], columns='Dept',values='Salary')
print(table2)
print("----------------------------------------------")
