digits=input("enter the digits along with the string:")
count=0
for char in digits:
    if char.isdigit():
        count=count+1
print(f"the number of digits in the string is:{count}")        
    