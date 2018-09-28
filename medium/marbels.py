def binom(t,c):
    if 2*c > t:
        c = t - c
    if c < 0:
        return 0
    bn = 1
    for v in range(t-c+1, t+1):
        bn *= v
    for v in range(2,c+1):
        bn //= v
    return bn

for _ in range(int(input())):
    n,k = map(int,input().split())

    print(binom(n-1,k-1))
        