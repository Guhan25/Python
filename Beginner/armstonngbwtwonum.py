n=int(input(""))
m=int(input(""))
for num in range(n,m+1):
   sum=0
   l=num
   while l>0:
       k=l%10
       sum+=k**3
       l//=10
   if (num==sum):
       print(num)
