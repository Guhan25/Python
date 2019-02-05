b=[]
n=int(input())
for i in range(1,n+1):
    c=int(input())
    b.append(c)
b.sort()
print(b[n-1])
