r=[]
n=int(input("Type the number"))
d=0
for i in range (1,n+1) :
    if n%i==0 :
        d=d+1
        r.append(i)
print("The number of divisors are: ",d)
print("The divisors of a number are :",r)
