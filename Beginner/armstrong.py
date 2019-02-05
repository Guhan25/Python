n =12
sum=0 
p=n 
while p > 0: 
  l=(p%10) 
  sum+=l** 3 
  p//= 10 
if(n==sum): 
  print("yes") 
else: 
  print("no")
