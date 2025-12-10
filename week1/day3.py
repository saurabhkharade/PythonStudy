arrayListData = ['Saurabh',55,97,1.5,'Programming','keeda']

print(arrayListData[1])   # Prints the element at index 1 → 55

print(arrayListData[0], type(arrayListData[0]))
# Prints the first element and its type → 'Saurabh' <class 'str'>

print(arrayListData[4], arrayListData[-1])
# Prints element at index 4 and last element → 'Programming' 'keeda'

arrayListData[2] = "Coding"
# Replaces the value 97 (index 2) with "Coding"

print(arrayListData)

arrayListData.append('Developer')
# Adds 'Developer' at the end of the list

print(arrayListData)

arrayListData.insert(6,'Android Developer')
# Inserts at index 6 (before last item)

print(arrayListData)

print(arrayListData.index('Android Developer'))
# Finds the index of the element 'Android Developer'

arrayListData.pop(1)
# Removes element at index 1 → removes 55

print(arrayListData)

arrayListData.pop()
# Removes the last element of the list ('Developer')

print(arrayListData)

arrayListData.remove(1.5)
# Removes the FIRST occurrence of the value 1.5 from the list
# We use remove(1.5) because 1.5 is still present in the list,
# and this command deletes that specific value (not by index)

print(arrayListData)


arrayL3 = [1,2,5,4,8,7,4,4,5,4,1,4,11,1,2,4,5,2,5,2,]
print(len(arrayL3)) ##length for your list
print(arrayL3)

print(arrayL3.count(5))
arrayL3.clear()
print(arrayL3)


arrayListDatas = ('Saurabh',55,97,1.5,'Programming','keeda')
print(arrayListDatas,type(arrayListDatas))
print(arrayListDatas[1])


#type casting converted tuple to list  fur muttion
Rec = (12345,12346,12347)
print(Rec,type(Rec))
Rec1 = list(Rec)
print(Rec1,type(Rec1))
Rec1[0]=15000
print(Rec1,type(Rec1))
Rec= tuple(Rec1)
print(Rec,type(Rec))