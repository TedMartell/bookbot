bookfile = "C:/Users/borje/workspace/github.com/TedMartell/bookbot/books/frankenstein.txt" 
def main():
    with open(bookfile) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    letter_count = {}
    for character in file_contents.lower():
        if character in letter_count:
           letter_count[character] += 1
        else:
            letter_count[character] = 1
    return letter_count

def print_report(text):
    letter_list = []
    letter_count = count_letters(text)
    for c in letter_count.keys():
        if c.isalpha():
            letter_list.append({"letter": c, "num": letter_count[c]})
    letter_list.sort(reverse=True, key=sort_on)    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    for letter in letter_list:
        print(f"The {letter["letter"]} character was found {letter["num"]} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

text = main()
print_report(text)


            
        




