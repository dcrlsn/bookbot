from collections import Counter
from functools import reduce

def main():
    book_path = "./books/frankenstein.txt"
    book_text = read_text(book_path)
    word_count = count_words(book_text)
    letter_count = count_letters(book_text)
    report = generate_report(letter_count, book_path)

def read_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(string):
    word_count = len(string.split())
    return word_count

def count_letters(string):
    counts = Counter(string.lower())
    return counts

def sort_on(dict):
    return dict["num"]

def generate_report(dict, book_path):
    mutated_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    report = f"--- Begin report of {book_path} ---\n"
    report += reduce(lambda acc, x: acc + f"'{x[0]}' character was found {x[1]} times.\n" if x[0].isalpha() else acc, mutated_dict, "") 
    report += "--- End report ---"
    print(report)


main()
