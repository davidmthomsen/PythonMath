from random import randint

def number_game():
    number = randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("What's your guess? "))
    while guess:
        if number == guess:
            print("That's correct! The number was ", number)
            break
        elif number > guess:
            print("Nope. Higher.")
        else:
            print("Nope. Lower")
        guess = int(input("What's your guess? "))



def greet():
    name = input("What's your name: ")
    if name == "Peter":
        print("That's my name, too!")
    else:
        print("Hello, ",name)

greet()
number_game()
