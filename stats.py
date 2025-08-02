



def prettify_results(chars, word_count, filepath):
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {filepath}\n")
    print("----------- Word Count ----------\n")
    print(f"found {word_count} total words.\n")
    print("--------- Character Count -------\n")
    chars = sorted(chars.items(),  reverse=True)
    for char in chars:
        print(f"{char}: {chars.count[char]}") 

def count_characters(filepath):
    char_dict = {}
    book = get_book_text(filepath).lower()
    for char in book:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


def get_word_count(filepath):
    book = get_book_text(filepath)
    words = book.split()
    return len(words)

def get_book_text(filepath):
    """Read the content of a book from a file and return it as a string."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content