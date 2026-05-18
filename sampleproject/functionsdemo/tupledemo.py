# 9. Write a function for a given tuple which has String elements, concatenate all elements and display?

def concatenate_elements(tup):
    str=""
    for item in tup:
        str=str+item+" "
    print(str)



tupnew=("Sun","Mon","tues","Wed","Thur","Fri","Sat")
concatenate_elements(tupnew)