def main():
    file_path = "books/frankenstein.txt"
    book = file_print(file_path)
    num_words = words_total(book)
    counter_char = get_char_dict(book)
    sorted_chars = sorting_data(counter_char)



    #report, part 11
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char_data in sorted_chars:
        print(f"The '{char_data['char']}' character was found {char_data['count']} times")

    print("--- End Report ---")


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

def sorting_data(char_dict):
    #makes dictionary list of dict
    char_list = [{"char": char, "count": count} for char, count in char_dict.items()]

    #sorting list on count, desc
    char_list.sort(key=lambda x: x["count"], reverse=True)

    #Filtering non-alpha chars
    alpha_char = [item for item in char_list if item ["char"].isalpha()]

    return alpha_char





main()
#main to finish the code and tell it to execute what's above
