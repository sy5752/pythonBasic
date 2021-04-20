import random
# 방법1

mine = input("가위/바위/보를 선택하시오")
print(mine)
 
com=""
rnd = random.random()
print(rnd)
if rnd > 0.333 :
    com = "가위"
elif rnd > 0.333 :
    com = "바위"
else:
    com = "보"    
 
result = ""
if mine == com:
    result = "비겼습니다."
elif mine=="가위" and com=="보":  
    result = "이겼습니다."
elif mine=="보" and com=="바위":  
    result = "이겼습니다."
elif mine=="바위" and com=="가위":  
    result = "이겼습니다."     
else:
    result = "졌습니다."
     
print("com : ", com)
print("mine : ", mine)
print("result : ", result)

# 방법2

mine = input("가위/바위/보를 선택하시오")


com=""
rnd = random.randint(1,3)

if rnd == 1 :
    com = "가위"
elif rnd == 2 :
    com = "바위"
else:
    com = "보"    

result = ""
if mine == com:
    result = "비겼습니다."
elif mine=="가위" and com=="보":  
    result = "이겼습니다."
elif mine=="보" and com=="바위":  
    result = "이겼습니다."
elif mine=="바위" and com=="가위":  
    result = "이겼습니다."     
else:
    result = "졌습니다."
    
print("com : ", com)
print("mine : ", mine)
print("result : ", result)

