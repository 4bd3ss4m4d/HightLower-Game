from game_data import data
import art
import random
from replit import clear

def check_result(i, answer):
    name_searches = data[i]['follower_count']
    next_name_searches = data[i+1]['follower_count']
    if answer == 'A':
        if name_searches >= next_name_searches:
            return True
        else:
            return False
    elif answer == 'B':
        if next_name_searches >= name_searches:
            return True
        else:
            return False 

def main():
    print(art.logo)
    print("Welcome to the Higher Lower Game!\n")


    # shuffle the data list
    random.shuffle(data)

    score = 0

    for i in range(len(data)):
        name = data[i]['name']
        description = data[i]['description']
        country = data[i]['country']
        if (i + 1) < len(data):
            next_name = data[i+1]['name']
            next_description = data[i+1]['description']
            next_country = data[i+1]['country']
            print(f"Compare A: {name}, a {description}, from {country}.")
            print(art.vs)
            print(f"Against B: {next_name}, a {next_description}, from {next_country}.")
            answer = input("\nType 'A' or 'B': ")
        else:
            print("Congrats! You've completed the game!")
            print(f"Your final score is {score}")
        checking = check_result(i, answer )
        if checking == False:
            print("Wrong answer!")
            print(f"Your final score is {score}")
            break
        score += 1
        clear()
        print(f"Score : {score}")
main()
