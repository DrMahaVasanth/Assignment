num1=0
num2=1
i=0
print("Fibonocci series between 0 and 50")
while (i<10):
    if i<=1:
        fib=i
    else:
        fib= num1+num2 
        num1=num2
        num2=fib
    print (fib)
    i+=1
