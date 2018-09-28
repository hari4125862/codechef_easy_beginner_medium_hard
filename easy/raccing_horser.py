t=int(input())
for i in range (t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    arr2=[]
    for i in range(n-1):
        arr2.append(arr[i+1]-arr[i])
    print(min(arr2))
    