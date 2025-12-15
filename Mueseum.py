s=str(input())
s="a"+s
c=0
#print(s)
for i in range(1,len(s)):
    c+= min(abs(ord(s[i])-ord(s[i-1])), abs(26 - abs(ord(s[i])-ord(s[i-1]))) )
print(c)