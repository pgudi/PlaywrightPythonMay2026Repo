A={0,2,4,6}
B={1,2,3,4,5}

print("Set A :",A)
print("Set B :",B)

# Union Operation always provides All unique elements, It never provides duplicate elements
print("Union :", A | B)

# Intersect , It provides common Elements
print("Intersect :", A & B)

# Minus: It provides elements from first set , the same elements whic hare not available in second set
print("Minus A - B :", A - B)
print("Minus B - A :", B - A)

# Symetric Diffference (Inverse of Intersect)
print("Symetric Difference :", A ^ B)