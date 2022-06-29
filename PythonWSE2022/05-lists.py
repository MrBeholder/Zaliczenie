myList = [20, "marca", 2022, "Narzędzia ..."]

print(myList)
print(myList[0]) #pierwszy element
print(myList[-1]) #ostatni element

myList[-1] = "Przemiot: "
print(myList)
myList[3] = myList[3] + "Narzędzia procesu tworzenia oprogramowania"
print(myList)


myList.insert(3, "8:15 - 10:15")
print("Insert:", myList)
myList.append("WSE")
print("Append:", myList)

myList.remove(2022)
print("Remove:", myList)
myList.pop(0)
print("POP:", myList)

print("Ilość elementów:", len(myList))