# f non-decreasing and x to be inserted at the last possible order preserving position.
def mybinsearch3(f,l,r,x):
    ans=-1
    if f(r)<=x:
        ans=r
    if f(l)<=x:    
        while l<r:
            m= ((l+r)//2) + 1
            if f(m)>x:
                r=m
            else:
                l=m 
        ans = m
