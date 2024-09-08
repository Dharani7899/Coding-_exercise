str=input("enter the string:").lower()
ch1=input("enter the char1:")
ch2=input("enter the char2:")
res=""
for i in str:
    if(i==ch1):
        res=res+ch2
    elif(i==ch2):
        res=res+ch1
    else:
        res=res+i
print(res)            


  