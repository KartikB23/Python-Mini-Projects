import random
print("Welcome to the Random Number Guessing Game.")
top_of_range = input("Type a number: ")
guess = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Enter a number greater than 0 next time.")
        quit()
else:
    print("Please Enter a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
while True:
    guess += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number next time.")
        continue

    if user_guess == random_number:
        print("You Got it in " + str(guess) + " guesses.")
        break
    else:
        if user_guess < random_number:
            print("Try a higher number.")
        if user_guess > random_number:
            print("Try a lower number")

