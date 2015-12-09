# -*- coding: utf-8 -*-

def take_beer(fridge, number=1):
    if not isinstance(fridge, dict):
        raise TypeError("Invalid fridge")

    if "beer" not in fridge:
        raise ValueError("No more beer:(")

    if number > fridge["beer"]:
        raise ValueError("Not enough beer:(")

    fridge["beer"] -= number


if __name__ == "__main__":
    fridge1 = {}
    fridge2 = "fridge_as_string"
    for fridge in (fridge1, fridge2):
        try:
            print("I wanna drink 1 bottle of beer...")
            take_beer(fridge)
            print("Oooh, great!")
        except TypeError as e:
            print("TypeError {} occured".format(e))
        except ValueError as e:
            print("ValueError {} occured".format(e))
