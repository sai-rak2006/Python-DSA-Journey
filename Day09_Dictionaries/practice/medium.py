words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for ch in words:
    if ch in count:
        count[ch] = count[ch] + 1
    else:
        count[ch] = 1

for key, value in count.items():
    print(key, ":", value)