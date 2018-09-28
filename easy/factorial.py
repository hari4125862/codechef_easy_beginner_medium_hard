n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
for i in arr:
	a=5
	n=0
	q=0
	while i/a>0:
		n=i//a
		q+=n
		a*=5
	print(q)