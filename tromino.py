def howmanyways2(n):
    dpa=[]
    dpb=[]
    dpa.append(0)
    dpb.append(0)
    dpa.append(1)
    dpb.append(1)
    dpa.append(2)
    dpb.append(2)
    for i in range(3,n+1):
        dpb.append(dpb[i-1] + dpa[i-1])
        dpa.append(dpa[i-1] + dpa[i-2] + (2* dpb[i-2]))
    #print(dpa)
    #print(dpb)
    return dpa[n]