import random

def rollDice(sides):
    return random.randint(1, sides)

acceptableAnswers = ["yes","yep","si", "grasias"]
number = 6 

while 'True':
    result = (rollDice(number))
    print(result)
    if result == 4:
        print("******************you win $10000000")
    roll_again = input("would you like to roll again? (Yes/No):").lower()
    if roll_again not in acceptableAnswers:       
         break