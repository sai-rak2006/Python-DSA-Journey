numbers=[1,2,3,4,5,6,7]
numbers.insert(1, 100)
print(numbers)

numbers = [2, 4, 6, 8]
s=0
for n in numbers:
    s=s+n
print(s)

numbers = [12, 45, 8, 99, 21]
max=numbers[0]
for n in numbers:
    if n>max:
        max=n
print(max)
