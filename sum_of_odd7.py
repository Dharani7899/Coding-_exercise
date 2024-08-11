lis=[1,2,3,4,5,6,7,8]
odd=[]
count=0
for i in lis:
    if(i%2!=0):
        odd.append(i)
print(odd)
con=0
for i in odd:
    con=con+i
print("th sum of the odd element in the list is:",con)    


