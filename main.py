from stats import count_words, sort_by_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = count_words(sys.argv[1])
    char_count = sort_by_count(sys.argv[1])
    counts_str = "\n".join(char_count)
    message = f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{counts_str}
============= END ==============="""
    return message 
if __name__ == "__main__":
    print(main())

    