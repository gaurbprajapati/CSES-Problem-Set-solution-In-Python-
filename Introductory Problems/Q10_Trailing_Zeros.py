def findTrailingZeros(n):
    # Negative Number Edge Case
    if(n < 0):
        return -1
 
    # Initialize result
    count = 0
 
    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n
 
    return count
 
 
n=int(input())
print(findTrailingZeros(n))