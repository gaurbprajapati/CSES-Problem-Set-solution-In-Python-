import itertools

s=input()
p=list(itertools.permutations(s))
print(len(set(p)))
l=[]
for  i in set(p):
    l.append("".join(i))
for i in sorted(l):
    print(i)