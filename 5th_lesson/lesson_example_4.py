# -*- coding: utf-8 -*-

def take_beer(fridge, number=1):
    if "beer" not in fridge:
        raise Exception("No beer at all:(")

    if number > fridge["beer"]:
        raise Exception("Not enough beer:(")

    fridge["beer"] -= number

def take_rum(fridge):
    fridge["rum"] -= 1


if __name__ == "__main__":
    fridge = {
        "beer": 2,
        "rum": 0,
    }
    print("I wanna drink 1 bottle of beer...")
    take_beer(fridge)
    print("Oooh, great!")
    print("I wanna drink 2 bottle of beer...")
    try:
        take_beer(fridge, 2)
    except Exception as e:
        print("Error: {}. Let's continue".format(e))
    finally:
        print("Ye-ho-ho! And the bottle of rum!")
        take_rum(fridge)

