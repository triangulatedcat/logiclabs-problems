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