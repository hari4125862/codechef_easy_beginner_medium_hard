t=int(input())
for i in range(t):
    n=int(input())
    a=map(int,input().split())
    n=1
    count=0
    for i in a:
        n *=i
    for i in range(1, n + 1):
        if n % i == 0:
            count+=1
    print(count)
    




        



