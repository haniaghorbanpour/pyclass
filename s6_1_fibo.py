def fibonacci(adad):
    list=[0,1]
    for i in range(adad):
        list.append(list[i]+list[i+1])
    print(list[adad-1])
fibonacci(int(input()))
