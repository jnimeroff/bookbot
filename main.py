def extract_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read()
            #print(words)
    except FileNotFoundError:
        print(f'The file {file_path} was not found. Please check the path and try again.')
    return(words)

def word_count(words):
    wc = 0
    for word in words.split():
        wc += 1
    return(wc)

def character_count(words):
    cc = {}
    lowercase_words = words.lower()
    for character in lowercase_words:
        if character.isalpha():
            if character in cc:
                cc[character] += 1
            else:
                cc[character] = 1
    return(cc)

def pretty_print(cc):
    for c in cc:
        print(f"The '{c}' character was found {cc[c]} times")

def main():
    file_path = 'books/frankenstein.txt'
    print(f"--- Begin report of {file_path} ---")
    words = extract_words(file_path)
    #print(f"Content: {words}")
    wc = word_count(words)
    #print(f"Words: {wc}")
    print(f"{wc} words found in the document")
    print()
    cc = character_count(words)
    #print(f"Characters: {cc}")
    scc = dict(sorted(cc.items(), key=lambda x:x[1], reverse=True))
    #print(f"Characters: {scc}")
    pretty_print(scc)
    print(f"--- End Report ---")

main()