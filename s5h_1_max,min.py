first_number=int(input("enter your first number: "))
second_number=int(input("enter your second number: "))
if first_number>second_number:
    max=first_number
    min=second_number
else:
    max=second_number
    min=first_number
while(max!=min):
    print(max)
    max=max-1
print(min)
