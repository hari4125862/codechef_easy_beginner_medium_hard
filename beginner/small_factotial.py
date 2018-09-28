testc=int(input())
for i in range(testc):
    num=int(input())
    fac=1
    if num>0:
        for i in range(1,num+1):
            fac=fac*i
        print(fac)
    elif num<=0:
        print(0)