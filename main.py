from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_list
def get_book_text(book_path):
    with open(book_path) as f:
         read_book = f.read()
         return read_book

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) # Get the text
    num_words = get_num_words(text) # Pass the text to get_num_words
    char_count = get_num_char(text) # Pass the text to get_num_char
    sorted_list = get_sorted_list(char_count) # Pass the dictionary char_count to get_sorted_list
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    print(sorted_list)
main() # Call main to start the program