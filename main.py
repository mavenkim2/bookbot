def count_words(file):
    return len(file.split())


def count_letters(file):
    character_counts = {}
    for char in file:
        character_counts[char.lower()] = character_counts.get(char.lower(), 0) + 1
    return character_counts


def print_report(text):
    print("--- Begin report of books/frankenstein.txt")
    print(f"{count_words(text)} words found in the document")
    counts = count_letters(text)
    letters = list(counts.items())
    letters.sort(reverse=True, key=lambda x: x[1])

    for char, count in letters:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)


main()
