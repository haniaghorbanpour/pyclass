classA = {"Ali" , "Hania" , "Farzaneh" , "Tina" , "Saeed"}
classB = {"Hania" , "Farzaneh" , "Tina" , "Mahsa"}

#tamam daneshjo ha chap shan
classA.update(classB)
print(classA)

#daneshjo haye moshtarak chap shan
classC=classA.intersection(classB)
print(f"{classC} ina moshtarakan")

#chap kardan 1 kelas faghat A
classD1=(classA-classC)

#chap kardan 1 kelas faghat B
classD2=(classB-classC)

print(f"{classD1.union(classD2)} ina faghat 1 class daran")
