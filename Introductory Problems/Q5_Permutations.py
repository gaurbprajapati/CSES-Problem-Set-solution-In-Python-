n=int(input())
if n==1:
    print(n)
elif n<=3:
    print("NO SOLUTION")
else:
    for i in range (n-1,0,-2):
        print(i,end=' ')
    for j in range (n,0,-2):
        print(j,end=" ")