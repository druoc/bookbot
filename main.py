def main():
        book_text = get_book_text()
        book_char_count = count_characters(book_text)
        report(book_char_count)
        
def get_book_text():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()
        return file_contents
                
             
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
                    
    return(char_count)

def report(char_dict):
    print("---Beginning book report---")
    


main()
    
    

