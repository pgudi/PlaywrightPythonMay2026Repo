num=10

def display_numbers():
    global num
    print(num)
    if(num<20):
        num=num+1
        display_numbers()

display_numbers()
print("--------------------")
rev=40
def display_numbers_rev():
    global rev
    print(rev)
    if(rev>30):
        rev=rev-1
        display_numbers_rev()

display_numbers_rev()

