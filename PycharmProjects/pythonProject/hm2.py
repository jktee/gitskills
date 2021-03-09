import numpy as np
import matplotlib.pyplot as plt
alpha=5 #alpha=0.5/alpha=1/alpha=5
x=1 #x=2/x=3/x=4

def myf(x):#公式函数
    y=np.sqrt((5+4*np.cos(x))/4)+np.sqrt((5-4*np.cos(x))/4)
    return(y)

def myparf(x):#求偏微分函数
    return(-4*np.sin(x)/np.sqrt(5+4*np.cos(x))+4*np.sin(x)/np.sqrt(5-4*np.cos(x)))

save1 = [];save2=[]
#未迭代
save1.append(1);save2.append(myf(1))
#开始迭代
for i in range(0,100):
    x = x - alpha * myparf(x)
    save1.append(x)
    save2.append(myf(x))
    print("第%d次迭代：x=%f，y=%f" % (i+1 , x, myf(x)))

plt.plot(save1,label='x')
plt.plot(save2,label='y')
plt.legend(loc=0)
plt.show()

#输出x、y最小值
