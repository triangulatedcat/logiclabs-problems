import sys
import random
sys.setrecursionlimit(100000)

#mybubblesort fails on subtask3
def mybubblesort(arr, i=0, n=None): 
    if n==None:
        n=len(arr)
        
    if n == 1:
        return arr

    if i == n - 1:
        return mybubblesort(arr, 0, n - 1)

    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return mybubblesort(arr, i + 1, n)

#def myinsertionsort(arr,i=0,):
#    if 


#"""
c="Yes"
for j in range(random.randint(1,10)):
    a=[]
    for i in range(random.randint(1,20)):
        a.append(random.randint(-10,10))
    b = a.copy()
    mybubblesort(b)
    a.sort()
    if  a != b :
       print(b)
       print(a)
       c="No"
       
print(c)            

"""
t = int(input())
passing_marks=[]
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    mybubblesort(a)
    passing_marks.append(a[-x] - 1)
   
for i in passing_marks:
    print(i)
#"""