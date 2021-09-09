def factorial(n):
    if n==1:
         return 1
    zarb = n*factorial(n-1)
    return zarb

print(factorial(int(input("enter your number: "))))
