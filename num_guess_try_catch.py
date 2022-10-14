#!/usr/bin/env python3
# Created By: Jeremiah omoike
# Date: October 14 2022
# This program takes a guess number from user and checks if it is correct
import random


def main():
    # input user will pick a number between 0 and 9
    print("I am thinking of a number between 0 and 9.")
    print("can you guess what it is?")
    user_input = int(input("Please guess here:"))

    # process and display
    random_variable = random.randint(0, 9)
    try:
        user_input == random_variable
        print("congratulations, you are correct!") 
    except Exception:
        print("This is not an integer")
    else:
        print(
            "sorry, {} was not correct. The correct answer is {}".format(
                user_input, random_variable))
    finally:
        print("Thank you for playing my game")
    
            
if __name__ == "__main__":
    main()
