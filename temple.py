# cook your dish here
s = int(input())
lengths = []
heights = []
temple = []

for i in range(s):
    n = int(input())
    lengths.append(n)
    localheights = list(map(int, input().split()))
    heights.append(localheights)

for i in range(s):
    temple.append("yes")
    r = len(heights[i])
    
    if r%2 == 0:
        temple[i] = "no"
        continue
    else:
        r1 = (r-1)//2
        for j in range(r1+1):
            if heights[i][j] == j+1 and heights[i][r-1-j] == heights[i][j]:
                continue
            else:
                temple[i]="no"
            
for i in range(s):
    print(temple[i])
            
        