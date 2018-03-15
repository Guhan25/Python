a=int(input("Enter the number:"))
if(a<0):
    print("wrong input")
else:
    for i in range(a):
        print(i+1)
    z=int(input("enter no.of digits to be added:"))
    sum=z*(z+1)/2
    print (sum)
