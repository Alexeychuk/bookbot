def count_characters(file_contents):
    countDict = {}

    for char in file_contents.lower():
        if char in countDict:
            countDict[char] += 1
        else:
            countDict[char] = 1

    return countDict



def main():
    bookPath = "books/frankenstein.txt"
    with open(bookPath) as f:
        file_contents = f.read()
        print(f"--- Begin report of {bookPath} ---")
        print(f"{len(file_contents.split())} words found in the document\n")
        characters = count_characters(file_contents)


        for char in characters:
            print(f"The '{char}' character was found {characters[char]} times")



main()