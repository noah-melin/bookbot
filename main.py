def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    book_path = 'path/to/book.txt'
    book_text = get_book_text(book_path)
    print(book_text)

main()