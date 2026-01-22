
secret_number = 4
print("i'm thinking of a number between 1 and 10")

#count guesses
guesses = 0

guess = int(input("enter your guess: "))
guesses += 1

while guess != secret_number:
    if guess < secret_number:
        print("too low! try again.")
    else:
        print("too high! try again.")
    guess = int(input("enter your guess: "))
    guesses += 1

("Number was {secret_number}.")
print(f"It took you {guesses} guesses.")
