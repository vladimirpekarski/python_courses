# -*- coding: utf-8 -*-


def take_beer(fridge, number=1):
    if "beer" not in fridge:
        raise Exception('No more beer :(')

    if number > fridge['beer']:
        raise Exception('Not enough beer:(')

    fridge['beer'] -= number

if __name__ == '__main__':
    fridge = {
        'beer': 200,
        'milk': 1,
        'meat': 3,
    }

    print('I wann drink 1 bottle of beer...')
    take_beer(fridge)
    print('Oooh, great!')
    print('I wann drink 2 bottle of bear...')
    take_beer(fridge, 10)
