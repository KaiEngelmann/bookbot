from collections import defaultdict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    text = get_book_text(book)
    count = len(text.split())
    return count


def count_characters(book):
    text = get_book_text(book).lower()
    letter_counts = defaultdict(int)
    for char in text:
        if char.isalpha():
            letter_counts[char] += 1
    return dict(letter_counts)