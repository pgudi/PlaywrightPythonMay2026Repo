sum=0

def sum_numbers():
    global sum
    for i in range(1,11):
        sum=sum+i
    print("Sum of Numbers :",sum)

sum_numbers()