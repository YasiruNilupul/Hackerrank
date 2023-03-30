k=3
m=10000
list1=[5,4]
list2=[7,8,9]
list3=[5,7,8,9,10]
s=0
x=10
high_s=0
for i in list1:
    for j in list2:
        for l in list3:
            s=i**2+j**2+l**2
            s=s%m
            if s>high_s:
                high_s=s
            s=0
print(high_s)
