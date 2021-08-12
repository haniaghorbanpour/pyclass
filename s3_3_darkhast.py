def mostatil (tol , arz , darkhast):
    if darkhast == "masahat":
        print(tol * arz)
    if darkhast == "mohit":
        print(2*(tol + arz))

a = int(input())
b = int(input())
c = input()

mostatil(a,b,c)
