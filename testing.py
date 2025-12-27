import math
import random
def mybinsearch1(a,l,r,x):
        ans=-1
        while l<=r:
                m = l + ((r-l)//2)
                if a[l]==x:
                    ans=l
                    #print(l,m,r,ans)
                    break
                elif a[m] >=  x:
                    r=m
                    #print(l,m,r)
                else:
                    l=m+1
                    #print(l,m,r)
        return ans
def first(low, high, key):
    
    ans = -1;

    while (low <= high):
        mid = low + ((high - low + 1) // 2);
        midVal = a[mid];

        if (midVal < key):

            # if mid is less than key, all elements
            # in range [low, mid] are also less
            # so we now search in [mid + 1, high]
            low = mid + 1;
        
        elif (midVal > key):

            # if mid is greater than key, all elements 
            # in range [mid + 1, high] are also greater
            # so we now search in [low, mid - 1]
            high = mid - 1;
        
        elif (midVal == key):

            # if mid is equal to key, we note down
            #  the last found index then we search 
            # for more in left side of mid
            # so we now search in [low, mid - 1]
            ans = mid;
            high = mid - 1;

    return ans;
"""
a=[]
for j in range(500000):
    a.append(random.randint(-100,100))
k=random.randint(0,499999)
a.sort()
x=a[k]
#print(p)
#print(x)
if first(0,499999,x) == mybinsearch1(a,0,499999,x) :
    print("Ok")
else:
    print("Oops")
"""
