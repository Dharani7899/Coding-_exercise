lis=[5,10,15,20,25]
count=0
a=int(input("enter the value:"))
for i in lis:
    if i%a==0:
        count+=1
print(count)        