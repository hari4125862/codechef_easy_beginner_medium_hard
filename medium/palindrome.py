import sys
def plaindrome(num):
 for i in range(num+1,sys.maxsize):
  if str(num) == str(num)[::-1]:
   return num
   break
n=int(input())
while(n):
 print(plaindrome(int(input())))
 n=n-1
