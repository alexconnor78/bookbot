from stats import get_word_count
from stats import get_book_text
from stats import count_characters
from stats import prettify_results



def main():
    """Main function to execute the book reading."""
    filepath = 'books/frankenstein.txt'  # Path to the book file
    get_book = get_book_text(filepath)
    #print(get_book)
    num_words = get_word_count(filepath)
    #print(f'{num_words} words found in the document.')
    chars = count_characters(get_book)
    #print(f'Character counts: {chars}')
    prettify_results(chars, num_words, filepath)
main()