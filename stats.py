def sort_on(items):
    return items['count']

def return_sorted_dict(dict):
    return_list = []
    i = 0
    for key, value in dict.items():
        return_list.append({'char': key, 'count': value})
    return return_list

def prettify_results(chars, word_count, filepath):
    dicto = return_sorted_dict(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    dicto.sort(reverse=True, key=sort_on)
    for item in dicto:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

            
                
def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_word_count(filepath):
    book = get_book_text(filepath)
    words = book.split()
    return len(words)

def get_book_text(filepath):
    """Read the content of a book from a file and return it as a string."""
    with open(filepath, 'r') as file:
        content = file.read()
    return content