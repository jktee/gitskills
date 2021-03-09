import pandas as pd
import numpy as np
data=pd.read_csv('/Users/kevin/Documents/homework/data_x1x2x3y.csv')
d1=data[0:80]
#打乱顺序
from sklearn.utils import shuffle
d2=shuffle(d1)
#初始化
w=np.array([0,0,0,0]);k=0;t=0
for n in range(len(d2)):
    yx=np.array([d2.iloc[n][3],d2.iloc[n][0],d2.iloc[n][1],d2.iloc[n][2]])
    if np.dot(w.T,yx) <= 0:
        w=w+yx
        k=k+1
    t=t+1
    if t == 200:
        break
print(w)
