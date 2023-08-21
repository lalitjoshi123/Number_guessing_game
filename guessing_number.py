# Number guessing game
actual_number=int(input("Enter a number:"))
attempts=0
while True:
    attempts+=1
    guess=int(input("Guess the number:"))
    if guess<actual_number:
        print("your guess is too low")
    elif guess>actual_number:
        print("Your guess was too high")
    else:
        print("You guessed the number in",attempts,"attempts")
        break
print("Thanks for playing")