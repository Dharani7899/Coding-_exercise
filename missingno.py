def num(*n):
    sum=0
    z=list(n)
    length=len(z)+1
    for i in z:
        sum=sum+i
    print(sum)
    first_n=length*(length+1)//2
    missing=first_n-sum
    return missing   
    
    






n=[1,3,4,5]    
print("the missing value is",num(*n))