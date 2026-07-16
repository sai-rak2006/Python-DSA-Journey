secret = 7
i=0

while i<3:
    guess = int(input("Guess the number: " ))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong!")
        i=i+1
if i == 3:
    print("Game Over!")
    print("The secret number was", secret)