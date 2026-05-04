num=int(input("Enter The Number :\n"))
fact=1
for i in range(num,0,-1):
    fact=fact * i

print("Factorial of ",num, " is ", fact)