import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#单变量线性回归
path='ex1data1.txt'
data=pd.read_csv(path,header=None,names=['Population','Profit'])
data.head()
data.plot(kind='scatter',x='Population',y='Profit',figsize=(12,8))
plt.show()

#损失函数
def computeCost(X,y,theta):
    inner=np.power((X*theta.T)-y,2)
    return np.sum(inner)/(2*len(X))

data.insert(0,'Ones',1)
cols=data.shape[1]
X=data.iloc[:,0:cols-1]
y=data.iloc[:,cols-1:cols]
X=np.matrix(X.values)
y=np.matrix(y.values)
theta=np.matrix(np.array([0,0]))
computeCost(X,y,theta)

#梯度下降
def gradientDescent(X,y,theta,alpha,iters):
    temp=np.matrix(np.zeros(theta.shape))
    parameters=int(theta.ravel().shape[1])
    cost=np.zeros(iters)
    for i in range(iters):
        error=(X*theta.T)-y
        for j in range(parameters):
            term=np.multiply(error,X[:,j])
            temp[0,j]=theta[0,j]-(alpha/len(X))*np.sum(term)
        theta=temp
        cost[i]=computeCost(X,y,theta)
    return theta,cost
alpha=0.01
iters=1000
g,cost=gradientDescent(X,y,theta,alpha,iters)
print(g)
print(computeCost(X,y,g))
#画图查看拟合
x=np.linspace(data.Population.min(),data.Population.max(),100)
f=g[0,0]+(g[0,1]*x)
fig,ax=plt.subplots(figsize=(12,8))
ax.plot(x,f,'r',label='Prediction')
ax.scatter(data.Population,data.Profit,label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit VS. Population Size')
plt.show()
#画图查看迭代损失的下降
fig,ax=plt.subplots(figsize=(12,8))
ax.plot(np.arange(iters),cost,'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Traning Epoch')
plt.show()




#多变量线性回归
path='ex1data2.txt'
data2=pd.read_csv(path,header=None,names=['Size','Bedrooms','Price'])
data2=(data2-data2.mean())/data2.std()

data2.insert(0,'Ones',1)
cols=data2.shape[1]
X2=data2.iloc[:,0:cols-1]
y2=data2.iloc[:,cols-1:cols]
X2=np.matrix(X2.values)
y2=np.matrix(y2.values)
theta2=np.matrix(np.array([0,0,0]))
g2,cost2=gradientDescent(X2,y2,theta2,alpha,iters)
print(computeCost(X2,y2,g2))

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(np.arange(iters), cost2, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()


























