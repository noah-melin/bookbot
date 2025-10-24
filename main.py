import sys
from stats import number_of_words,sorted_characters

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        content = file.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path} ...")
    print(f"----------- Word Count ----------\nFound {number_of_words(book_text)} total words")
    print(f"--------- Character Count -------\n{sorted_characters(book_text)}")
    
main()