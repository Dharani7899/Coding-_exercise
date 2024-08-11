lis = [10, 20, 20, 80, 90, 50, 50,50]
count = 0
tar_elem = int(input("Enter the element to know how many times it is repeated in your list: "))

for i in lis:
    if i == tar_elem:
        count += 1

print(f"{tar_elem} occurs {count} times")
