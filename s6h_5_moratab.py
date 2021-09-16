num=[1,3,7,2,5,4,9,8]
print(len(num))
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        print(num[i], num[j], max)
        if num[j]>=num[i]:
            max=num[j]
            num[j]=num[i]
            num[i]=max
print(num)
