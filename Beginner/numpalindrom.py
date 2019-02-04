n=int(input("Enter number:"))
t=n
c=0
while(n>0):
    div=n%10
    c=c*10+div
    n=n//10
if(t==c):
    print("yes")
else:
    print("no")
