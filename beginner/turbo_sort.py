n=int(input())
a=[]
for i in range(n):
	t=int(input())
	a.append(t)
a.sort()
for i in range(n):
	print(a[i])