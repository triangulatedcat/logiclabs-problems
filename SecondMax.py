n = int(input()) #number of test cases

OutputList=[] #this will store the second max for each input list

for i in range(n):
    
    InputList = list(map(int, input().split())) 
    OrderedInputList = [InputList[0]]
    
    #pick the j^th element of the inputlist
    for j in range(1,len(InputList)):
        
        #append/insert the j^th inputlist element into the orderedinputlist
        for k in range(len(OrderedInputList)):  
            if InputList[j] <= OrderedInputList[k]:
                OrderedInputList.insert(k,InputList[j])
                break
            elif k == len(OrderedInputList) - 1:
                OrderedInputList.append(InputList[j])
                break
            
    #Now append the second max element to OutputList
    OutputList.append(OrderedInputList[-2])
#    print(OrderedInputList)        
for i in range(n):
    print(OutputList[i])
