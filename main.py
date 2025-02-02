def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_report(text,book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    textiter = text.lower()
    char_dict = {}
    char_list  =[]
    for i in textiter:
        if i in char_dict:
            char_dict[i] += 1
        else:
            if i.isalpha():
                char_dict[i] = 1
    for character in char_dict:
        num = char_dict[character]
        char_list.append({"letter":character, "num":num})

    return char_list

def sort_on(dict):
    return dict["num"]

def book_report(book_text,path):
    word_count  = wc(book_text)
    character_count = get_character_count(book_text)
    character_count.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for character in character_count:
        letter = character["letter"]
        num = character["num"]
        print(f"The '{letter}' character was found {num} times")
    print("--- End Report ---")


def wc(file_content):
    words = file_content.split()
    return len(words)

main()