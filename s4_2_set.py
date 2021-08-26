list1=["amir" , "ali" , "hania" , "maryam" , "sara"]
list2=["nima" , "ali" , "hania"]

list1.extend(list2)
print(set(list1))
print("ina kelas daran")
#set(list1).update(set(list2))
#print(set(list1))
#set(list1).union(set(list2))
#print(set(list1))
print(set(list1).intersection(set(list2)))
print(set(list1).union(set(list2)))
print(set(list1) - set(list1).intersection(set(list2)))
