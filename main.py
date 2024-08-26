def main():
    #Text file location to analyze
    book_path = "books/frankenstein.txt"
    #Grab copy of book text for analysis
    text = get_book_text(book_path)
    #Print report of book path using file path, number of words, and char occurence dictionary.
    print_book_stats(book_path, count_words(text), count_letters(text))

def get_book_text(path):
    #Open and return book text
    with open(path) as f:
        return f.read()

def count_words(text):
    #Return number of words in book text, split on spaces
    return len(text.split())
    
def count_letters(text):
    #Avoid duplicate dict keys by converting text to lowercase
    lower_text = text.lower()
    #Create dictionary for characters 
    chars = {}
    #Iterate over chars, incrementing if they exist, creating them with value of 1 if they don't
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    #Return dictionary of characters paired with number of occurences
    return chars

def print_book_stats(path, num_words, char_dict):
    #Sort chars dict as list of tuples with lambda function to sort on value, descending order.
    sorted_chars = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    #Print report
    print(f"Report on {path}")
    print()
    print(f"There are {num_words} words in this text")
    print()
    for key, value in sorted_chars:
        #Print alpha characters only in report on char frequency
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print()
    print("End of Report")
    return None

main()
    

