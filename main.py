from stats import get_num_words
from stats import get_num_char
def get_book_text(book_path):
    with open(book_path) as f:
         read_book = f.read()
         return read_book

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) # Get the text
    num_words = get_num_words(text) # Pass the text to get_num_words
    char_count = get_num_char(text)
    print(f"{num_words} words found in the document")
    print(char_count)
    
        
main() # Call main to start the program