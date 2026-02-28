# Number of Distinct integers
"""
n = int(input())
b = list(map(int,input().split()))
b.sort()
c=1
for i in range(0, len(b)-1):
    if b[i] < b[i+1]:
        c+=1
#print (b)
print(c)
"""

#Anton vs Danik chess
"""
n = int(input())
verdicts = str(input())
a,d = 0,0
for char in verdicts:
    if char == "A":
        a+=1
    else:
        d+=1
if d<a:
    print("Anton")
elif a<d:
    print("Danik")
else:
    print("Friendship")
"""

#Limak Bear heavy
"""
import math
a,b = map(int,input().split())
print(math.floor(math.log(b/a,3/2))+1)
"""

#Petya and friends
"""
n = int(input())
d=0
for i in range(n):
    a,b,c = map(int,input().split())
    if a+b+c > 1:
        d+=1
print(d)
"""

#Beautiful matrix
"""
a=[]
for i in range(5):
    b = list(map(int, input().split()))
    a.append(b)
found=0
i=0  
while ( i < 5 ):
    if found==1:
        break
    j=0
    while (j < 5):
        if (a[i][j] == 1):
            r,c = i,j
            found = 1
            break
        j+=1
    i+=1    
print(abs(2-r)+abs(2-c))
"""

#Gravity flip
"""
n = int(input())
a = list(map(int,input().split()))
a.sort()
print(*a)
"""

#Petya strings
"""
a = str(input())
b = str(input())
c=a.lower()
d=b.lower()
if c<d:
    print(-1)
elif c>d:
    print(1)
else:
    print(0)
"""

#Vasya word
"""
s=str(input())
c=0
for char in s:
    if 'A' <= char <= 'Z':
        c+=1
    else: 
        c-=1
if c>0:
    print(s.upper())
else:
print(s.lower())
"""

#Magnets
"""
n=int(input())
b=""
c=1
for i in range(n):
    a=str(input())
    if b != "":
        if b != a:
            c+=1
    b=a
print(c)
"""

#Stones
"""
n=int(input())
s=str(input())
c=0
if len(s)>1:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c+=1
print(c)
"""

#Police recruits
"""
n=int(input())
a=list(map(int,input().split()))
fc=0
uc=0
for i in range(len(a)):
    if a[i]>0:
        fc+=a[i]
    else:
        if fc==0:
            uc+=1
        else:
            fc-=1
print(uc)    
"""
#Chef stones game
"""
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # your code goes here
    c=0
    b=sorted(a,reverse=True)
    for i in range(0,len(b),2):
        c+=b[i]
    print(c)
"""
#Limak nice sequence
"""
# cook your dish here
t= int(input())
c=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c.append(a[-1])
    #print(a)
    for j in range(len(a)-1):
        if (a[j+1]-a[j]) == 0:
            c[i]=a[j]
     #       print(c)
            break
        elif (a[j+1]-a[j]) > 1 and j==0:
            c[i]=a[j]
      #      print(c)
            break
for j in range(t):
    print(c[j])
"""
#Zigzag array
"""
t=int(input())
c=[]
d=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d.append(a)

for j in range(t):    
    if (len(d[j])==1):
        c.append(d[j])
        continue
    i=0
    a=d[j]
    while (i < len(a)-1):
        if ((i%2)==0 and a[i]>a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
        elif ((i%2)==1 and a[i]<a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
        i+=1
        #print(a)
    c.append(a)
for r in range(t):
    print(*c[r])
"""     
#Way too long words
"""
n = int(input())
strgs=[]
nstrgs=[]
for i in range (n):
    s=str(input())
    strgs.append(s)
    if len(s) > 10:
        nstrgs.append(s[0] + str(len(s)-2) + s[len(s)-1])
    else:
        nstrgs.append(s)
for j in range(n):
    print(nstrgs[j])
"""
"""
s=str(input())
l = list(map(str,s.split('+')))
l.sort()
print("+".join(l)) 
"""
"""
s=str(input())
print(s[0].upper() + s[1:])
"""
"""
k,n,w = map(int,input().split())
c=(k*w*(w+1)/2) - n
if c>0:
    print(int(c))
else:
    print(0)
"""
"""
n,k = map(int,input().split())
while (k > 0):
    c = n%10
   # print(n,k)
    if c == 0:
        n = int(n/10)
        k-=1
       # print(n,k)
    else:
        n = n - 1
        k-=1
      #  print(n,k)
print(n) 
"""
"""
s= str(input())
t= str(input())
rev_s= s[::-1]
if rev_s == t:
    print("YES")
else:
    print("NO")
"""
"""
n=int(input())
s=[]
t=0
for r in range(n):
    a,b = map(int,input().split())
    t+= (b-a)
    s.append(t)
s.sort()
print(s[-1])
"""
# cook your dish here
"""
import math
t=int(input())
h=[]
for r in range(t):
    n=int(input())
    s=math.floor(math.sqrt(2*n))
    while (s**2 + s > 2*n):
        s-=1
    h.append(s)
for r in range(t):
    print(h[r])       
"""
"""
import math
t=int(input())
c=[]

for r in range(t):
    n,k = map(int,input().split())
    l=list(map(int,input().split()))
    #carrots.append(l)
    j=0
    i=0
    while (i<len(l)):
        if (k**math.floor(math.log(l[i],k)) == l[i]):
            j+=1
        i+=1
    c.append(j)
    
for r in range(t):
    print(c[r])
   
#In search easy problem
t = int(input())
ans=""Easy""
l = list(map(int,input().split()))
for r in range(t):
    if l[r]==1:
        ans=""Hard""
        break
    else:
        continue
print(ans)

n = int(input())
l=[]
ans=0
for r in range(n):
    l.append(list(map(int,input().split())))
    if l[r][1] - l[r][0] > 1:
       ans+=1
print(ans)

#Inverse array
n=int(input())
l=list(map(int,input().split()))
ans=[0]*(len(l))
for r in range(len(l)):
    ans[l[r]-1]=r+1
    #print(*ans)
print(*ans)


from decimal import Decimal, getcontext
getcontext().prec = 7

n=int(input())
l=list(map(int,input().split()))                 
print(Decimal(sum(l))/Decimal(n))


a=str(input())
b=str(input())
c=[]
for r in range(len(a)):
    c.append(int(a[r])^int(b[r]))
print(*c,sep='')

l=list(map(int,input().split()))
s=set(l)
print(len(l)-len(s))
"""
n=int(input())
l=list(map(int,input().split()))
l.sort()
s=sum(l)
i=len(l)-1
ans=0
r=0
if s<n:
    ans=-1
else:
    while (r<n):
        r+=l[i]
        i-=1
    ans = len(l) - 1 - i    
print(ans)

