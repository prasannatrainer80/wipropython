import pandas as pd
import numpy as np

x=pd.Series("Wipro",index=[1,2,3,4])
print(x)
print(x.index)

x1=pd.Series(data=["Raj","Manoj","Kiran","Nalini"],index=[0,1,2,3])
print(x1)
print(x1.size)

x2=pd.Series(data=["Raj","Manoj","Kiran","Nalini"],index=["zero","one","two","three"])
print(x2)
print(x2.index)
print(x2.shape)
print(x2.size)
