m,n = map(int, input().split())
k=m*n
if k%2 == 1:
    print((m*n - 1)//2)
else:
    print ((m*n)//2)