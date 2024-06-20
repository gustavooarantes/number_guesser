import random

random_number = random.randint(1, 10)

print("=============================================================")
print("WELCOME TO THE GAME!")
print("You should guess a random number between 1 and 10. Good Luck!")
print("=============================================================\n")

def pick_a_number():
    while True:
        number = input("Choose a number: ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= 10:
                break
            else:
                print("You should pick a number between 1 and 10!")
        else:
            print("You must enter a valid number!")
    return number

chosen_number = pick_a_number()

if random_number == chosen_number:
    print("You've guessed right! Congrats!")
    quit()
else:
    print("You're wrong! Sorry :(")