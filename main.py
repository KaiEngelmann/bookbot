from stats import count_words, sort_by_count

def main():
    word_count = count_words("/mnt/d/bookbot/books/frankenstein.txt")
    char_count = sort_by_count("/mnt/d/bookbot/books/frankenstein.txt")
    counts_str = "\n".join(char_count)
    message = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{counts_str}
============= END ==============="""
    return message 
if __name__ == "__main__":
    print(main())

    