def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_book_stats(book_path,count_words(text),count_letters(text))

    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())
    
def count_letters(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def print_book_stats(path,num_words, char_dict):
    sorted_chars = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    print(f"Report on {path}")
    print()
    print(f"There are {num_words} words in this text")
    print()
    for key, value in sorted_chars:
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("End of Report")
    return None


main()
    

