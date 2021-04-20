# 100에서 200까지의 합

sum = 0
# 방법1

# for i in range(101):
#     sum = sum+i
# print(sum)
#     
# sum1 = 0
# for i in range(201):
#     sum1 = sum1+i
# print(sum1)
# 
# print(sum1 - sum)

# 방법2

for i in range(201):
    if i >= 100:
        sum += i
print(sum)

# for i in range(101):
#     sum += (i+100)
# print("sum:"+str(sum))
    
    