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
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {filepath}\n")
    print("----------- Word Count ----------\n")
    print(f"found {word_count} total words.\n")
    print("--------- Character Count -------\n")
    dicto.sort(reverse=True, key=sort_on)
    for item in dicto:
        for item2 in item.keys():
            print(type(item2))
            
                
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