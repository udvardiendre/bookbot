import sys
from stats import get_num_words, get_each_character, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
        return file_contents

def get_num_of_words(text):
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def main():
    if len(sys.argv) == 2: 
        text = get_book_text(sys.argv[1])
        # get_num_of_words(text)
        character_dictionary = get_each_character(text)
        sorted_dict = sort_dictionary(character_dictionary)
        # print(character_dictionary)
        # print(sorted_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        print("--------- Character Count -------")
        for element in sorted_dict:
            if element["character"].isalpha():
                print(f"{element['character']}: {element['number']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()