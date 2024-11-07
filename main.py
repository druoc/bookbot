def main():
        book_text = get_book_text()
        book_word_count = word_count(book_text)
        book_count_dict = count_characters(book_text)
        book_chars_list_sorted = sort_dicts_to_list(book_count_dict)

        report(book_word_count, book_chars_list_sorted)
        
def get_book_text():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()
        return file_contents         
             
def word_count(book):
    count_of_words = len(book.split())
    return count_of_words
        
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

def sort_on(d):
    return d["num"]

def sort_dicts_to_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(num_of_words, book_chars_list):
    print("---Beginning book report---")
    print(f"This book contains {num_of_words} words")
    
    for item in book_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("---End report---")
    
    


main()
    
    

