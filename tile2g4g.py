def howmanyways(n,m):
    dp=[]
    dp.append(1)
    for i in range(1,n+1):
        if i<m:
            dp.append(1)
        else:
            dp.append(dp[i-m]+dp[i-1])
    return dp[n]


def countWays(n, m):
    
    # table to store values
    # of subproblems
    count =[]
    for i in range(n + 2):
        count.append(0)
        count[0] = 0
    
    # Fill the table upto value n
    for i in range(1, n + 1):
    
        # recurrence relation
        if (i > m):
            count[i] = count[i-1] + count[i-m]
        
        # base cases 
        elif (i < m or i == 1): 
            count[i] = 1

        # i = = m 
        else:
            count[i] = 2
    
    
    # required number of ways
    return (count[n])