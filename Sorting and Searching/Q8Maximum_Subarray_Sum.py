def max_sum(arr):
    if max(arr)<0:
        return max(arr)
    c=0
    s=0
    for i in range (len(arr)):
        if c>=0:
            c=c+arr[i]
        else:
            c=arr[i]
        s=max(s,c)
    return s
            
 
 
n=int(input())
arr=list(map(int,input().split()))
print(max_sum(arr))