# The operations commute. 
# Prove inductively that equality of salaries achievable.
# The difference in original salaries equals the difference in the number of operations they undergo.
# Follows that the necc&suff number of operations equals the sum over i of w_i - min[w_i].

t = int(input())
answer=[]

for i in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    
#Find minimum value in the list w    
    min_w = w[0]
    for j in range(1,len(w)):
        if  w[j] < min_w :
            min_w = w[j]
    
    ans=0
    for j in range(len(w)):
        ans += (w[j] - min_w)
    
    answer.append(ans)
        
for i in range(t):
    print(answer[i])