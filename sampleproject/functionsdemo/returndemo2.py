def show_list_elements():
    list=[10,20,30,40,50,60]
    for item in list:
        print(item, end="  ")
    print()
show_list_elements()

print("-------------------------")

def get_list_elements():
    list=[100,200,300,400,500,600]
    return list

elements =get_list_elements()
print(elements)
# read all Elements
for i in range(0,len(elements)):
    print(elements[i], end=" ")
print()
# find sum of Elements
sum=0
for i in range(0,len(elements)):
    sum=sum+elements[i]
print("Sum of All Eleemnts :",sum)

# Read First half of Eleemnts
j=0
while(j<len(elements)/2):
    print(elements[j])
    j=j+1