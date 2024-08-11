arr=[4,5,6,7,8,9,10]
n=int(input("enter the element to be checked whether it is existed in the array:"))
found=0
for i in arr:
  if i==n:
    found=True
    break
if found:
  print("element exist in the array")    
else:
  print("element not exist in the array")  