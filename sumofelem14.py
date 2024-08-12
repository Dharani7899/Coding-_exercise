arr=[2,3,4,5,6,78,7]
values=int(input("enter the value:"))
sum=0
 
for element in arr:
    if element>values:
        sum+=element
print(f"the sum of the elements greater than {values} is {sum}")         
