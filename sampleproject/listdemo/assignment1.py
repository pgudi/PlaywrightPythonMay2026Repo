# 1. Programmatically add Even numbers 10 to 30 in to list and read Elements from List?
'''
step 1: make sure we can display numbers 10 to 30
Step 2: display Even numbers in between 10 to 30
Step 3: Create List and Add Each Even umbers into List
Step 4: Read Even numbers from List
'''
list=[]
for i in range(10,31):
    if(i % 2 ==0):
        list.append(i)


for item in list:
    print(item, end=" ")
