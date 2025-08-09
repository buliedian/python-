import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw=RandomWalk(150000)
    rw.fill_walk()
    plt.style.use('classic')
    
    """
    fig,ax=plt.subplots()
    ax.plot(rw.x_values,rw.y_values,linewidth=0.5)
    
    """

    
    fig,ax=plt.subplots(figsize=(12,9),dpi=128)
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=2,
edgecolors='none')

    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=30)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=30)
    
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("是否继续？y/n    :")
    if keep_running=='n':
        break
