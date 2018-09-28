t=int(input())
while t:
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr2=[]
    chef=[]
    asst=[]
    for i in range(n):
        arr2.append(i+1)
    for j in arr:
        arr2.remove(j)
    arr2.sort()
    for i in range(0,len(arr2),2):
        chef.append(arr2[i])
        if (i+1) < len(arr2):
            asst.append(arr2[i+1])
        elif (i+1) == len(arr2):
            break
    for i in chef:
        print(i,end=' ')
    print('')
    for i in asst:
        print(i,end=' ')
    t=t-1
        
            

        
        
        
        
        
        
        
    









    
