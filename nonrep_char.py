from collections import Counter

def fnr(stingg):
    dict_key=Counter(stingg)
    for i in stingg:
        if dict_key[i]==1:
            return i
  






stingg="dharani"
print(fnr(stingg))    

























