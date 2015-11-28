__author__ = 'vladimir.pekarsky'

def find_secret_message(text):
    upper_letters = []
    for letter in text:
        if letter.isupper():
            upper_letters.append(letter)

    return ''.join(upper_letters)

print(find_secret_message('How are you? Eh, ok. Low or Lower? Ohhh.'))
print(find_secret_message('hello world!'))
print(find_secret_message('Please make sure Your Third Homework has been dONe'))

