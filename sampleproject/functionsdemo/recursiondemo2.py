
def get_factorial(num):
    if(num==1):
        return 1
    return num * get_factorial(num-1)

v1=get_factorial(4)
v2=get_factorial(5)
v3=get_factorial(6)
print(v1,v2,v3)