#Find the largest Number
numbers=[5,25,10,15]
largest = numbers[0]
for num in numbers:
    if num>largest:
        largest=num
        print("largest:",largest)