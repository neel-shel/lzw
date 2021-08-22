# takes text string and return compressed string
def compress(text):
    split_text = list(text)
    print(split_text)
    
    result = ''
    string = ''
    dictionary = {}

    for ch in split_text:
        print(string+ch)

        if string+ch in dictionary:
            string += ch
        else:
            result += string
            temp = string + ch
            dictionary.add(temp)
            string = ch

    return result

# takes text string and returns decompressed string
def decompress(text):
    # TODO
    pass
