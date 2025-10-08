#使用KMeans进行图像压缩
import numpy as np
import matplotlib.pyplot as plt

#步骤1：确定所属的集合。返回值为X的所有样本的集合，为数组。
def  find_closest_centroids(X,centroids):
    #centroids为样本中心点
    num=X.shape[0]
    K=centroids.shape[0]
    idx=np.zeros(X.shape[0],dtype=int)
    for i in range(num):
        distance=[]
        for j in range(K):
            norm_ij=np.linalg.norm(X[i]-centroids[j])
            distance.append(norm_ij)
        idx[i]=np.argmin(distance)
    return idx

#步骤2：计算样本中心点位置
def compute_centroids(X,idx,K):
    m,n=X.shape
    centroids=np.zeros((K,n))
    for k in range(K):
        points=X[idx==k]#获取聚类k的所有样本
        centroids[k]=np.mean(points,axis=0)#重新计算样本k的中心点
    return centroids

#步骤3:迭代后样本所属的聚类和聚类中心脏点
def run_kMeans(X,initial_centroids,max_iters=10):
    m,n=X.shape
    K=initial_centroids.shape[0]

    centroids=initial_centroids
    previous_centroids=centroids
    idx=np.zeros(m)

    for i in range(max_iters):
        idx=find_closest_centroids(X,centroids)
        centroids=compute_centroids(X,idx,K)
    return centroids,idx
#步骤4：随机初始化中心点
def kMeans_init_centroids(X,K):
    randidx=np.random.permutation(X.shape[0])
    centroids=X[randidx[:K]]
    return centroids
#图片的处理
path=r"E:\Desktop\photo\壁纸图片\最后的.png"
original_img=plt.imread(path)
original_img=original_img.astype(float)/255
X_img=np.reshape(original_img,(-1,3))
K=16
max_iters=10
initial_centroids=kMeans_init_centroids(X_img,K)
centroids,idx=run_kMeans(X_img,initial_centroids,max_iters)
X_recovered=centroids[idx,:]
X_recovered=np.reshape(X_recovered,original_img.shape)
fig,ax=plt.subplots()
plt.axis('off')
ax.imshow(X_recovered*255)
ax.set_axis_off()
fig.savefig('thephoto_compress.png',bbox_inches='tight')







