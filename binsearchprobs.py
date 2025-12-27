
import math
def mybinsearch(a,l,r,x):
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
"""
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
"""

#Rectangles

w,h,n = map(int,input().split())
u=max(n*w+1,n*h+1)
l=math.floor(math.sqrt(n*w*h))-1
b=list( ((r//w)*(r//h) - n) for r in range(max(n*w+1,n*h+1)) ) 
x= mybinsearch(b,l,u,0)
print(x)
      



