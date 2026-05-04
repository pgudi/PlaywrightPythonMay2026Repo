fn=0
sn=1
print(fn, end=" ")
print(sn, end=" ")

for i in range(1,9):
    tn=fn+sn
    fn=sn
    sn=tn
    print(tn, end=" ")