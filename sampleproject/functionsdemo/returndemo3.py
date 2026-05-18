def get_prime_number_status(num):
    flag=0
    for i in range(2,num):
        if(num % i ==0):
            flag=flag+1
            break
    if(flag==0):
        return True
    else:
        return False

v1=get_prime_number_status(21)
print(v1)
# 12. Write a function to display sum of prime numbers in between 1 to 50
sum=0
for i in range(1, 51):
    if (get_prime_number_status(i)==True):
        sum=sum+i
print("sum of Prime Numbers in between 1 to 50 :",sum)
# 13. Write a function to display count of prime numbers in between 50 to 100
count=0
for j in range(50, 101):
    if (get_prime_number_status(j)==True):
        count=count+1
print("Count of Prime Numbers in between 50 to 100 :",count)
# 11. Write a function to display prime numbers in between 1 to 100
for k in range(1,101):
    if(get_prime_number_status(k)==True):
        print(k, end=" ")