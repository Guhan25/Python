n=int(input("Enter the number:"))
x=int(input("enter no.of digits to be added:"))
if(n<0):
    print("wrong input")
else:
    for i in range(n):
        print(i+1)
    sum=x*(x+1)/2
    print("the sum is ")
    print (sum)
