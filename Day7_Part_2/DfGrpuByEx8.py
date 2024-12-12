import numpy as np
import pandas as pd

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
result1=df.head(5)
print(result1)
result3=df.sort_values("Salary",ascending=False)
print(result3)
result2=df.sort_values("Salary",ascending=False).head(1)
print(result2)
result_max_5_sal=df.sort_values("Salary",ascending=False).head(5)
print("First Five Top employes based on Salary-Wise  ")
print(result_max_5_sal)