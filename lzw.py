# takes text string and return compressed string
def compress(text):
    split_text = list(text)
    
    result = []
    string = ''
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}

    for ch in split_text:
        if (string + ch) in dictionary:
            string = (string + ch)
        else:
            result.append(dictionary[string])
            dictionary[(string + ch)] = dictionary_size
            dictionary_size += 1
            string = ch

    if string:
        result.append(dictionary[string])

    return ','.join([str(i) for i in result])

# takes text string and returns decompressed string
def decompress(text):
    split_text = [int(i) for i in text.split(',')]

    result = ''
    dictionary_size = 256
    dictionary = {i: chr(i) for i in range(dictionary_size)}

    prev = chr(split_text.pop(0))
    result += prev
    for curr in split_text:
        if curr in dictionary:
            entry = dictionary[curr]
        elif curr == dictionary_size:
            entry = prev + prev[0]
        else:
            raise Exception("error!")
        result += entry

        dictionary[dictionary_size] = prev + entry[0]
        dictionary_size += 1

        prev = entry
    
    return result
