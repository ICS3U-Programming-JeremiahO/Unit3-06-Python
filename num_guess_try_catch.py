#!/usr/bin/env python3
# Created By: Jeremiah omoike
# Date: October 14 2022
# This program takes a guess number from user and checks if it is correct

import random


def main():
    # input user will pick a number between 0 and 9
    print("I am thinking of a number between 0 and 9.")
    print("Can you guess what it is?")
    user_input_as_string = input("Please guess here:")

    # set a variable to a random number from 0 to 9
    random_number = random.randint(0, 9)

    try:
        # cast user integer from a string to an int
        user_input_as_int = int(user_input_as_string)

        if user_input_as_int == random_number:
            print("Congratulations, you are correct!")
        else:
            print(
                "Sorry, {} was not correct. The correct answer is {}".format(
                    user_input_as_int, random_number
                )
            )
    except Exception:
        print("This is not an integer")
    finally:
        print("Thank you for playing my game")


if __name__ == "__main__":
    main()
