def main():
    file_path = "books/frankenstein.txt"
    book = file_print(file_path)
    num_words = words_total(book)
    counter_char = get_char_dict(book)
    
    #report, part 11
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

def file_print(path):
    with open(path) as f:
        file_contents = f.read()
        # file_contents now reads the entire text of the file ive specified

        return file_contents
        # returns the entire book

def words_total(book):
    words = len(book.split())
    #counts how many words total there are

    return words


def get_char_dict(file_contents):
    char_dict = {}
    for d in file_contents:
        lower_case = d.lower()
        if lower_case in char_dict:
            char_dict[lower_case] += 1
        else:
            char_dict[lower_case] = 1
    return char_dict

main()
#main to finish the code and tell it to execute what's above
