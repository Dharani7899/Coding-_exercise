def arrr(*n):
    s=set(n)
    print("the unduplicated list values are",list(s))
    
    
    
    
    
n=list(map(int,input("enter the array with duplicates:").split()))
arrr(*n)
    