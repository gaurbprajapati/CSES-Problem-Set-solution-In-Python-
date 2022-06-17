n=int(input())
l=list(map(int,input().split()))
s=sum(l)
s2=n*(n+1)/2
print(int(s2-s))