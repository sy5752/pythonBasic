import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure() # 새로운 figure를 생성해준다
ax = fig.gca(projection='3d') 

# test data
x = np.array([0,0,0,0,0]) # -10 ~ 10까지 1마다 찍음
y = np.array([0,1,2,3,4]) # np는 2차원 배열과 비슷

z1 = np.array([2,3,4,2,2])
# z2 = np.array([3,3,3,3,3])
# z3 = np.array([])-y * y

# plot test data
ax.plot(x, y, z1)
ax.plot(x+1, y, z1)
ax.plot(x+2, y, z1)

# ax.plot(x, y, z2)
# ax.plot(x, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()