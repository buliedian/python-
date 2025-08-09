import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
x=range(1,5001)
y=[x**3 for x in x]
plt.style.use('seaborn-v0_8-pastel')
fig,ax=plt.subplots()
ax.scatter(x,y,c='red',s=1)
ax.set_title("立方图",fontsize=12)
ax.set_xlabel("x",fontsize=12)
ax.set_ylabel("y",fontsize=12)
ax.tick_params(axis='both',which='major',labelsize=14)
plt.savefig("立方图.png",bbox_inches='tight')
