n=int(input())
b=str(input())
j=0
for item in b:
    if item == "1":
        j+=1
ans= n - (2*min(j, n-j))
print(ans)