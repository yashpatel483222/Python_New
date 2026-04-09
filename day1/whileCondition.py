a=10
while a<6:
    print(a,end="")
    a+=1
n = int(input("enter a number:"))
for i in range(2,n//2):
        if n%i==0:
            print("not prime ")
        else:
            print("prime")

            
        