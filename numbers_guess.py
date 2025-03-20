import random

top_of_run = input("Type the number here: ")

if top_of_run.isdigit():
    top_of_run=int(top_of_run)

    if top_of_run<=0:
        print("Type a number is greater than 0 next time.")
        quit()

else:
    print("Type a number next time.")
    quit()

random_number = random.randint(0,top_of_run)

guess_number = 0

while True:
    guess_number = guess_number + 1
    user_number = input("Guess the number: ")

    if user_number.isdigit():
        user_number=int(user_number)

    else:
        print("Please type a number next time.")
        continue

    if user_number == random_number:
        print("You got it")
        break

    elif user_number > random_number:
        print("You above the number.")

    elif user_number < random_number:
        print("you below the number.")

print("You guess it in",guess_number,"try.")


