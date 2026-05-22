class Person:
    fname="Santosh"
    age=22
    loc="California"


obj1=Person()
print(obj1.fname, obj1.age, obj1.loc)
print("First Name :",obj1.fname)
print("Age :",obj1.age)
print("Location :",obj1.loc)
print("--------------------")
print(Person.fname, Person.age, Person.loc)
print("First Name :",Person.fname)
print("Age :",Person.age)
print("Location :",Person.loc)