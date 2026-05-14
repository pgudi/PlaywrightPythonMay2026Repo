list1=["Apple",100,"Lotus",12.75,True,"Dog"]
# Reverse 
list1.reverse()
print(list1)

# Sort
list2=["Apple","Cow","Lotus","Orange","Dog"]
list2.sort()
print(list2)

# pop()
list3=["Apple",100,"Lotus",12.75,True,"Dog"]
print(list3.pop(3))

# insert()
list4=["Apple",100,"Lotus",12.75,True,"Dog"]
list4.insert(3,"Welcome")
print(list4)

# index
list5=["Apple",100,"Lotus",12.75,True,"Dog"]
print(list5.index("Dog"))

# clear
list6=["Apple",100,"Lotus",12.75,True,"Dog"]
list6.clear()
print(list6)


# copy
list7=[10,20,30,40]
list8=list7.copy()
print(list8)

# Extends
list9=[10,20,30,40]
list10=[50,60,70]
list9.extend(list10)
print(list9)

# count
list11=["Mango","Apple","Mango","Apple","Mango","Apple"]
print(list11.count("Mango"))