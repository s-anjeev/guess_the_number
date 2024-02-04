import pyfiglet
import random

# title
def print_title(text):
    font = pyfiglet.Figlet()
    title = font.renderText(text)
    print(title)
# difficulty
def level_of_difficulty():
    print("Level of difficulty you want")
    print("Easy")
    print("Hard")
    difficulty_level = input("Enter your level of difficulty :")
    if type(difficulty_level) == str:
        difficulty_level.lower()
        if difficulty_level == "easy":
            total_number_of_attempts = 5
        else:
            total_number_of_attempts = 3
        return total_number_of_attempts
    else:
        print("wrong input\nenter only strings")
# set number
def set_number(total_number_of_attempts):
    if total_number_of_attempts == 5:
        random_number = random.randint(0,10)
        print("number is between 0,10")
    else:
        random_number = random.randint(0,50)
        print("number is between 0,50")
    return random_number
# input number
def guess_number(random_number,total_number_of_attempts):
    print("you have ",total_number_of_attempts," attempts")
    user_attempts = 0
    while total_number_of_attempts > user_attempts:
        user_guess = input("Enter your guess :")
        if user_guess == random_number:
            print("you won")
        else:
            print("you lose")
        user_attempts+=1
            # hint for difficult level
        if  total_number_of_attempts == 3 and user_attempts == 2:
            print("Hint")
            hint = random.randint(1,3)
            print("number is greater than ",random_number-hint)
            print("number is less than ",random_number+hint)
# print title
print_title("Guess Number")
# set difficulty lervel
total_number_of_attempts = level_of_difficulty()
# set random number
random_number = set_number(total_number_of_attempts)
# guess random number
guess_number(random_number,total_number_of_attempts)