#Write a Python program to get a list, sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples
size=int(input("Enter the number of elements need to be added:"))
lst=[]
lst1=[]
lst_final=[]
for i in range(size):
    tup1=int(input("Enter the value to be added:"))
    tup2=int(input("Enter the value to be added:"))
    lst.append(tup1)
    lst1.append(tup2)
    lst_final=list(zip(lst,lst1))
print("OG list",lst_final)
length=len(lst_final)
for i in range(0,length):
    for j in range(0,length-i-1):
        if lst_final[j][1]>lst_final[j+1][1]:
            temp=lst_final[j]
            lst_final[j]=lst_final[j+1]
            lst_final[j+1]=temp
print("sorted list of tuples:",lst_final)


