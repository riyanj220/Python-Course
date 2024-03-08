import random

top_of_range = input("Type number to generate random number range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("please type a number next time")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Make A guess: "))
    if user_guess:
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please type a number larger than 0 next time.")

        else:
            if user_guess == random_number:
                print("You Got it!")
                break
            elif user_guess > random_number:
                print("You were above the number")
            else:
                print("you were below the number")

print("you got it in ", guesses, "guesses")
