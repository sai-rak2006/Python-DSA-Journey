marks=[23,45,67,98,12]
s=0
avg=0
for n in marks:
    s=s+n
    avg=s/5

min=marks[0]
for n in marks:
    if n<min:
        min=n
print("smallest:",min)
print("total:",s)
print("avrerage:",avg)

