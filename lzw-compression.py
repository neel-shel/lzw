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
            dictionary.append(string + ch)
            string = ch

    return result
