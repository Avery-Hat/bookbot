def main(): #start of "main"
    #open to access the file location, and "" are needed when specifying the location, set to f
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # file_contents now reads the entire text of the file ive specified
        print(file_contents)
        # prints the entire book

    words = len(file_contents.split())
    print(f"There are {words} words in this book's file.")



main()
#main to finish the code and tell it to execute what's above