import numpy as np


a = [1,2,3,4,5,6,7,8]
print(a)

b = np.reshape(a,[2,4])
b = b+1

print(b[1,2])

c = [
        [1,2,3,4],
        [5,6,7,8]
    ]
print(c[1][2]) # 2차원배열의 문법은 c[1][2] c[1,2]라고 쓰면 오류
 
# np.arange(1,10,1) 
# 1~10까지의 배열을 만들어줌 / 인공지능할때 사용함

A= np.ones((2,2))

print(A)