numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessFnums = []

for num in numbers:
    if num < 5: 
        lessFnums.append(num) 
        lessFnums.sort()

print("Orignal list: ",numbers)
print("New list: ",lessFnums)

