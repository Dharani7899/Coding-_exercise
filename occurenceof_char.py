words=input("enter the string:")
char=input("enter which character is to be checked:")
count=0
for c in words:
    if(c==char):
        count+=1
print(f"the occurence of the {char} is {count} times ")        