import numpy as np
import pandas as pd

a = pd.Series(data=[[1,2,3,4],[2,3,4],[4,3,2]],index=[0,1,2])
print(a)
print(a.shape)
b=pd.Series(data=[1,2,3,4,5,6],index=['a','b','c','1','2','3'])
# print(b)
print(b.shape)
print(a.ndim)
print(b.ndim)