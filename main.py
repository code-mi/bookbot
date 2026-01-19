from stats import count_char, count_words, sort_on


def get_book_text(book_name):
    # getting file contents of the book
    with open(book_name, "r") as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text(
        "books/frankenstein.txt"
    )  # counts how many words are in the book and prints the result
    word_count = count_words(book_text)
    # counting the chars in the book and prints them in a dict
    char_count = count_char(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    print("PLACEHOLDER")
    print(char_count)
    print("============= END ===============")


main()
