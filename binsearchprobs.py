

   def mybinsearch(a,l=0,r=-1,x):
        ans=-1
        if r==-1:
            r=len(a)-1
        else:
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



