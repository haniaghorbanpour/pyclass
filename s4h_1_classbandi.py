classA = ['Hanieh', 'Tina', 'Behrad', 'Bita', 'Neda','Elham']
classB =['Hanieh' , 'Tina', 'Behrad' ,'Amir']

setA=set(classA)
setB=set(classB)
print(f"{setA.union(setB)} hadeaghal 1 class daran")
print(f"{setA.intersection(setB)} har 2 class ro daran")
print(f"{setA.union(setB)-(setA.intersection(setB))} faghat 1 class daran")
