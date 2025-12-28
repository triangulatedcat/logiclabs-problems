def isyearpretty(x):
    if x<= n:
         return 0
    y=str(x)
    if len(y) == len(set(y)):
         return 1
    else:
         return 0

n=int(input())
for i in range(n+1,9999):
    if isyearpretty(i) ==1:
         k=i
         break
print(k)