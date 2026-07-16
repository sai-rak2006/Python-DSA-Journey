# Program to reverse a number

number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10          # Get the last digit
    reverse = reverse * 10 + digit
    number = number // 10        # Remove the last digit

print("Reversed number:", reverse)