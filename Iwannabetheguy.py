n=int(input())
little_X = list(map(int,input().split()))
little_Y = list(map(int,input().split()))
final= list(set(little_X[1:] + little_Y[1:]))
if len(final) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")