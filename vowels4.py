word=input("enter the string:").lower()
li=[]
count=0
for i in word:
    li.append(i)
    if(i=='a' or i=='e' or i=='i' or i=='o'or i=='u'):
     count+=1
print(count)     