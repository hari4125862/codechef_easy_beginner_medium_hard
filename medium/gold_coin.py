def rate(x):
    if x in dic:
        return dic[x]
    elif x//2 + x//3 + x//4 > x:
        dic[x] = rate(x//2) + rate(x//3) + rate(x//4)
        return dic[x]
    elif x//2 + x//3 + x//4 <= x:
        dic[x] = x
        return dic[x]

dic = {}
while 1:
    try:
       print(rate(int(input())))
    except:
        break