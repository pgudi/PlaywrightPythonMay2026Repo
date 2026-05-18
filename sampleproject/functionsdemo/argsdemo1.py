def addition(*args):
    sum=0
    for x in args:
        sum=sum+x
    print("Addition Result :",sum)

addition(10)

def show_students_names(*args):
    for name in args:
        print(name, end=" ")

show_students_names("Santosh","bharath","Akshay","Ganesh")