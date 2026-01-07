def get_book_text(book_name):
    # getting file contents of the book
    with open(book_name, "r") as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


main()
