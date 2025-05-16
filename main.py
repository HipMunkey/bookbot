from stats import get_word_count
from stats import get_count_per_char
from stats import sort_chars
import sys

def get_book_text(location):
    with open(location) as f:
        file_contents = f.read()

    return file_contents

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book = get_book_text(path)
    num_words = get_word_count(book)
    num_chars = get_count_per_char(book)
    sorted_num_chars = sort_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_num_chars:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["count"]}")

    print("============= END ===============")

main()