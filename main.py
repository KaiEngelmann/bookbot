def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    text = get_book_text(book)
    count = len(text.split())
    return count

def main():
    frankenstein = count_words("/mnt/d/bookbot/books/frankenstein.txt")
    return f"{frankenstein} words found in the document"

if __name__ == "__main__":
    print(main())

    