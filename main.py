def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = word_count(file_contents)
        num_characters = character_count(file_contents)
        print("--- Begin report of books/frakenstein.txt ---")
        print(f"{num_words} words found in the document")
        print()
        for i in range(0,len(num_characters)):
            print(f"The '{num_characters[i]["alpha"]}' character was found {num_characters[i]["num"]} times")
        print("--- End report ---")

def word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def character_count(file_contents):
    lowered_string = file_contents.lower()
    characters = {}
    for character in lowered_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    alpha_list = []
    for char in characters:
        if char.isalpha():
            alpha_list.append({"alpha": char, "num": characters[char]})
    alpha_list.sort(reverse=True, key=sort_on)
    return alpha_list

def sort_on(dict):
    return dict["num"]

main()
