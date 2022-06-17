# # n=int(input())
 
# from sympy import fu, re
 
 
def fun(s):
    if len(s)==1:
        return 1
    if len(set(s))==1:
        return len(s)
    c=0
    i=0
    a=[]
    while(i<len(s)):
        if s[i]==s[(i+1)%len(s)]:
            c=c+1
            i=i+1
        else:
            a.append(c)
            c=0
            i=i+1
    return (max(a)+1)
s=input()
print(fun(s))