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

def sort_by_count(book):
    counts = count_characters(book)
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    formatted_list = [f"{letter}: {count}" for letter, count in sorted_counts]
    return formatted_list