import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
print(sys.argv[1])
from stats import get_num_words
from stats import get_num_char
from stats import get_sorted_list
def get_book_text(book_path):
    with open(book_path) as f:
         read_book = f.read()
         return read_book

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path) # Get the text
    num_words = get_num_words(text) # Pass the text to get_num_words
    char_count = get_num_char(text) # Pass the text to get_num_char
    sorted_list = get_sorted_list(char_count) # Pass the dictionary char_count to get_sorted_list
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/*.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(item["char"]+":",item["num"])
   
main() # Call main to start the program