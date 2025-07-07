from stats import *  # Import the functions from stats.py
import sys # Import sys for system-specific parameters and functions

# Check if the user passed exactly one argument (sys.argv[0] is the script name)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()

    return file_contents


def main():
    # This is the main function that will be called when the script is run
    # It will call the get_book_text function with the file path as an argument
    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    number_of_words = num_words(book_text)
    print(f"Found {number_of_words} total words")
    print("----------- Character Count -----------")
    character_count = num_characters(book_text)
    #print(f"Character count: {character_count}")
    sorted_characters = sort_characters(character_count)
    for char in sorted_characters:
        print(char['char'] + ':',char['num'])
    print("============ END ============")
    
    



if __name__ == "__main__":
    main() # Call the main function to execute the script