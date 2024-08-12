lis=input("enter the strings:").split()
lis1=[]
for i in lis:
    lis1.append(i)
first=lis1[0]
rev=first[::-1]
if(first==rev):
    print("the first string, it is a palindrome")
else:
    print("it is not a palindrome")    
