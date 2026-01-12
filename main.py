from stats import count_char, count_words


def get_book_text(book_name):
    # getting file contents of the book
    with open(book_name, "r") as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    # counts how many words are in the book and prints the result
    word_count = count_words(book_text)
    print(f"Found {word_count} total words.")

    # counting the chars in the book and prints them in a dict
    char_count = count_char(book_text)
    print(f"{char_count}\n")
#test

main()
