# 6. Write a function for a given dictionary object read all key and values?

def read_key_value(dict):
    for k,v in dict.items():
        print(k," -> ",v)


x={"A":"Apple","B":"Ball","C":"Cat","D":"Donkey"}
read_key_value(x)