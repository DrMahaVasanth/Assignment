# Write a Python program to get a list, sorted in increasing order 
# by the last element in each tuple from a given list of non-empty tuples
lst=[(2,5),(1,2),(4,4),(2,3),(2,1)]
length=len(lst)
print("original list of tuple:",lst)
for i in range(0,length):
    for j in range(0,length-i-1):
        if lst[j][1]>lst[j+1][1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("sorted list of tuples:",lst)
