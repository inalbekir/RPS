import random

print("What do you choose?")
RPS = ["rock","paper","scissors"]

computers_choice = random.choice(RPS)

my_choice = input("Type 0 for rock, 1 for paper or 2 for scissors.")
if my_choice == "0":
    result = RPS[0]
    if result == computers_choice:
        print(computers_choice)
        print(result)
        print("It's a tie!")
    elif computers_choice == "paper":
        print(computers_choice)
        print(result)
        print("Computer won!")
    else:
        print(computers_choice)
        print(result)
        print("You won!")
elif my_choice == "1":
    result = RPS[1]
    if result == computers_choice:
        print(computers_choice)
        print(result)
        print("It's a tie!")
    elif computers_choice == "rock":
        print(computers_choice)
        print(result)
        print("You won!")
    else:
        print(computers_choice)
        print(result)
        print("Computer won!")
elif my_choice == "2":
    result = RPS[2]
    if result == computers_choice:
        print(computers_choice)
        print(result)
        print("It's a tie!")
    elif computers_choice == "rock":
        print(computers_choice)
        print(result)
        print("Computer won!")
    else:
        print(computers_choice)
        print(result)
        print("You won!")
else:
    print("Please enter a valid value.")



