lis=[23,44,5,6,66]
a=int(input("enter the element in the list to return their respective index:"))
for i in range(0,len(lis)):
    if lis[i]==a:
        print(f"the index of 23{a} is",i)
        break
    else:
        continue
 