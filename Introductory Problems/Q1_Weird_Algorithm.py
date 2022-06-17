# def fun(a):
a=int(input())
# x=[]
print(a,end=" ")
while(a!=1):
    if a%2==0:
        a=a//2
    else:
        a=a*3+1
    print(a,end=" ")