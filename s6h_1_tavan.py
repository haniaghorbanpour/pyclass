vorodi1=int(input("enter your first number: "))
vorodi2=int(input("enter your second number: "))
num=[]
start=vorodi1
hasele_zarb=0
def zarb(adad1,adad2):
    hasele_zarb=0
    for i in range(adad2):
        hasele_zarb += adad1
    return hasele_zarb
for i in range(vorodi2):
    num.append(vorodi1)
for i in range(1,len(num)):
    start=zarb(start,num[i])
print(f"{vorodi1} be tavan {vorodi2} mishavad {start}")
