#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user input 3 integers and displays the highest


def main():
    # this function lets the user input 3 integers and displays the highest

    # input
    integer_1 = input("Enter your first integer: ")
    integer_2 = input("Enter your second integer: ")
    integer_3 = input("Enter your third integer: ")

    # process & output
    try:
        integer_int_1 = int(integer_1)
        integer_int_2 = int(integer_2)
        integer_int_3 = int(integer_3)

        if integer_int_1 > integer_int_2 and integer_int_1 > integer_int_3:
            print("\nYour integer, {0}, is the largest!".format(integer_int_1))

        elif integer_int_2 > integer_int_1 and integer_int_2 > integer_int_3:
            print("\nYour integer, {0}, is the largest!".format(integer_int_2))

        elif integer_int_3 > integer_int_1 and integer_int_3 > integer_int_2:
            print("\nYour integer, {0}, is the largest!".format(integer_int_3))

        elif integer_int_1 == integer_int_2 == integer_int_3:
            print("\nYou entered three {0}s!".format(integer_int_1))

        elif integer_int_1 == integer_int_2:
            print("\nYou entered two {0}s!".format(integer_int_1))

        elif integer_int_1 == integer_int_3:
            print("\nYou entered two {0}s!".format(integer_int_1))

        elif integer_int_2 == integer_int_3:
            print("\nYou entered two {0}s!".format(integer_int_2))

    except Exception:
        print("\nYou have entered an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
