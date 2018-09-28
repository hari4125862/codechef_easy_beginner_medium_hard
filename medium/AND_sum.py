n=int(input())
arr=list(map(int, input().split()))
l=len(arr)
s=0
for i in range(1,l):
    for j in range(i):
        s=s+(arr[j] & arr[i])
print(s)