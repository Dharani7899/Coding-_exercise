arr=[2,3,4,5,78,100,6,7,8,10]
value=int(input("enter the value:"))
for i in arr:
    if i>value:
        print("the first greatest element in the array is:",i)
        break
