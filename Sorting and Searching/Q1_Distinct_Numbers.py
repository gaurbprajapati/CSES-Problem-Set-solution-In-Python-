# for i in range (int(input())):
a=int(input())
l=list(map(int,input().split()))[:a]
print(len(set(l)))