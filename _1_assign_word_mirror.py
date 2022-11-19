org_str=input("Enter any string:")
rev_str=""
length=len(org_str)
for i in org_str:
    a=org_str[-1]
    org_str=org_str[:-1]
    rev_str+=a
    print (rev_str)
print ("The reversed string is", rev_str)

