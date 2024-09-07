
def sum(numbers):
    global tot
    tot = 0  # Reset tot to 0 before summing
    for i in numbers:
        tot += i
    print(tot)

sum([1, 2, 3, 4])
