for i in range (int(input())):
    r,c=map(int,input().split())
    if c>r:
        if c%2==0:
            ans=(c-1)*(c-1)+1+(r-1)
        else:
            ans=c*c-(r-1)
    else:
        if r%2==1:
            ans=(r-1)*(r-1)+1+(c-1)
        else:
            ans=r*r-(c-1)
    print(ans)