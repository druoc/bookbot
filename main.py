def main():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()
        print(file_contents)
        word_count(file_contents)
        count_characters(file_contents)
             
def word_count(book):
    count_of_words = len(book.split())
    print(f"This book contains {count_of_words} words")
        
def count_characters(book):
    lowercase_book = book.lower()
    char_count = {}
    for char in lowercase_book:
        keys = char_count.keys()
        
        if char in keys:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    print(char_count)

main()
    
    

