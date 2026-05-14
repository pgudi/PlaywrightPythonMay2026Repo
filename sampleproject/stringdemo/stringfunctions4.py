str1="Mango Apple Grapes Ornage"
print(str1.split(" "))

# rsplit
str2="Apple,Mango,Ornage,Banana, Grapes"
print(str2.rsplit(","))

# zfill
str3="45"
print(str3.zfill(5))

# swapcase() 
str4="python PROGRAM"
print(str4.swapcase())

# len
str5="JAVA"
print(len(str5))

# lstrip
str6="     Java"
print("Before lstrip :",len(str6))
print("After lstrip:",len(str6.lstrip()))

# rstrip
str6="Java       "
print("Before rstrip :",len(str6))
print("After rstrip:",len(str6.rstrip()))