

# To get the input from the user and count the number of even and odd
lst_size=int(input("Enter the number of elements to be added in the list:"))
lst=[]
count=1
even_count=0
odd_count=0
for i in range(lst_size):
    value=int(input("Enter the value: "))
    lst.append(value)
    count+=1
    if value%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Count of even numbers:", even_count,"\nCount of odd numbers:", odd_count)
