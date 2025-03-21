import sys
# This makes sure you stop at 1 option
def check_arguments():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
check_arguments()
book_path = sys.argv[1]
print(f"Analyzing book from: {book_path}")
from stats import get_number_of_words
from stats import character_count
from stats import organized_characters



# This function is to read the frankenstein book

def get_book_text(path):
    with open(path) as file:
        contents = file.read()
    return contents

def main():
    
    # Defining What book.. duh it's frankenstein
    book_text = get_book_text(book_path)
    # use the get_number_of_words funtion in the from command
    word_count = get_number_of_words(book_text)
    character_totals = character_count(book_text)
    sorted_characters = organized_characters(character_totals)
    # print the result
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # Sorting the printing of letter counts
    for char_dict in sorted_characters:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    # calling main funtion
main()
