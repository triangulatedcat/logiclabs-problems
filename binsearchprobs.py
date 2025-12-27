
#import math
def mybinsearch1(a,l,r,x):
        ans=-1
        while l<=r:
                m = l + ((r-l)//2)
                if a[l]==x:
                    ans=l
                    break
                elif a[m] >=  x:
                    r=m
                else:
                    l=m+1
        return ans
def mybinsearch2(f,l,r,x):
        ans=-1
        while l<=r:
                m = l + ((r-l)//2)
                #print(l,m,r,n*w*h,l**2)
                if f(l)==x:
                    ans=l
                    break
                elif f(m) >=  x:
                    r=m
                else:
                    l=m+1
        return ans

def minsquaresize(x):
    y= (x//w)*(x//h) - n
    if y>=0:
        return 1
    else:
        return 0

w,h,n = map(int,input().split())
u=max(n*w+1,n*h+1)
v=max(w,h)
print(mybinsearch2(minsquaresize,v,u,1))