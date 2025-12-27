
import math
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

w,h,n = map(int,input().split())
u=max(n*w+1,n*h+1)
l=max(w,h)
#b=list( ((r//w)*(r//h) - n) for r in range(max(n*w+1,n*h+1)) ) 
#x= mybinsearch(b,l,u,0)
#print(x)
ans=-1
print(l,ans,u)
while l<=u:
                m = l + ((u-l)//2)
                print(l,m,u,ans)
                if ((l//w)*(l//h) - n)==0:
                    ans=l
                    break
                elif ((m//w)*(m//h) - n) >=  0:
                    u=m
                else:
                    l=m+1
                print(l,m,u,ans)
print(ans)
      



