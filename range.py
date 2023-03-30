first=input().split()
first=list(map(int, first))
m=first[1]
k=first[0]



all_lists=[]
for i in range(k):
    list1=input().split()
    list1=list(map(int, list1))
    list1.pop(0)
    all_lists.append(list1[:])

s=0
high_s=0

for i in all_lists[0]:
     for j in all_lists[1]:
         for l in all_lists[2]:
            s=i**2+j**2+l**2
            s=s%m
            if s>high_s:
                high_s=s
            s=0
print(high_s)
