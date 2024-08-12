words = input("Enter the string: ").split() 
final = words  

min_len = len(final[0])  
min_word = final[0]  

for i in range(1, len(final)): 
    if len(final[i]) > min_len:  
        min_len = len(final[i])  
        min_word = final[i]  

print(f"The longest hai i am out of the world struck between my mind and hert word is: {min_word} with length {min_len}")
