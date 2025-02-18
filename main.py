def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words_in_book = word_count(file_contents)
    characters = char_count(file_contents)
    report(characters, words_in_book)
    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def char_count(file_contents):
    lowered_str = file_contents.lower()
    char_dict = {}
    for i in lowered_str:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict

def report(char_dict, word_count):
    alpha_dict = {}
    char_list = []
    for i in char_dict:
        if i.isalpha():
            alpha_dict[i] = char_dict[i]
    for char, count in alpha_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document")
    for i in char_list:
        print(f"The '{i['char']}' character was found {i['count']} times")
    print("--- End report---")
    
def sort_on(dict):
    return dict["count"]


main()