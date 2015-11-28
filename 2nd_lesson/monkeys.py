__author__ = 'vladimir.pekarsky'

def monkey_checker(text, words):
    count_words = 0
    text = text.lower()
    for word in words:
        if word in text:
            count_words += 1
    print(count_words)


monkey_checker("How aresjfhdskfhskd you? how are", {"how", "are", "you", "hello"})
monkey_checker("asdas dasd asdadwqwkjwkjwkljqwkcoolasdasd", {"cool", "are", "you", "hello"})
