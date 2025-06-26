from stats import count_words, count_characters

def main():
    frankenstein = count_words("/mnt/d/bookbot/books/frankenstein.txt")
    char_count = count_characters("/mnt/d/bookbot/books/frankenstein.txt")
    return f"{frankenstein} words found in the document\n {char_count}"

if __name__ == "__main__":
    print(main())

    