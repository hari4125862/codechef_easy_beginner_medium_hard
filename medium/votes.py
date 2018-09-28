T = int(input())
for t in range(T):
    sum = 0 
    notpossible = 0
    n = int(input())
    n = 0
    for i in input().split():
        if int(i):
            n += 1
            sum += int(i)

    a = sum - 100
    if a >= 0 and a < n:
        print ("YES")
    else:
        print ("NO")
