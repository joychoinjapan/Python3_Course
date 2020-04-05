list1 = [('Shi',100), ('Yan', 75), ('Lou', 200), ('Plus', 80)]

sortedlist = sorted(list1, key=lambda item:item[1])

print(sortedlist)