stringy=input("enter the statement:").lower()
filter_string=''.join(char for char in stringy if char.isalnum())
reverse_string1=filter_string.replace(" ","")
reverse_string2=reverse_string1[::-1]
if(filter_string==reverse_string2):
    print("it is a palindrome")
else:
    print("it is not a palindrome")    
