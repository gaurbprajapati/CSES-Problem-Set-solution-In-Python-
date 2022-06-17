n=int(input())
l=list(map(int,input().split()))
 
a=0
for i in range (0,len(l)-1):
    if l[i]>l[i+1]:
        a=a+l[i]-l[i+1]
        
        l[i+1]=l[i+1]+l[i]-l[i+1]
print(a)
# print(l)