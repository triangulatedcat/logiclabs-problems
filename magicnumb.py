n=str(input())
i=0
curr=n[0]
while (i<len(n)) and (curr =="1" or curr=="14" or curr=="144"):
    if n[i]=="1":
        curr="1"
    else:
        curr=curr+n[i]
    i+=1
if (len(n)==i) and (curr =="1" or curr=="14" or curr=="144"):
    print("YES")
else:
    print("NO")