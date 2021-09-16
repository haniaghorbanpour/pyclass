names=['ali','mahsa','bita','tina','hania','neda','parsa','farzaneh']
vorodi=input("enter your name: ")
count = 0
for name in names:
    if name != vorodi:
        count+=1
    else:
        print(count)
