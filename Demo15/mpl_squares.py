import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
"""
squares=[0,1,4,9,16,25]
fig,ax=plt.subplots()#plot代表整张图，ax表示图中的各个图表
ax.plot(squares,linewidth=3)
#设置图标标题并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)
#设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)#刻度，
plt.show()
"""

"""
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)
#设置图标标题并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)
#设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)#刻度，
plt.show()
"""

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.style.use('seaborn-v0_8-pastel')
fig,ax=plt.subplots()
ax.plot(input_values,squares,linewidth=3)
#设置图标标题并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)
#设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)#刻度，
plt.show()