import sys
from os import path
from lzw import *

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("usage: lzw [-c|-d] <input_file_path> <output_file_path>")
        sys.exit()

    option = str(sys.argv[1])
    input_file = str(sys.argv[2])
    output_file = str(sys.argv[3])

    if not path.isfile(input_file):
        print(f"{input_file} not found!")
        sys.exit()

    if path.exists(output_file):
        print(f"{output_file} already exists!")
        sys.exit()

    if option == '-c': #compress
        file = open(input_file, "r")
        input_text = file.read()
        file.close()

        output_text = compress(input_text)

        file = open(output_file, "wb")
        file.write(output_text)
        file.close()
    elif option == '-d': #decompress
        file = open(input_file, "rb")
        input_text = file.read()
        file.close()

        output_text = decompress(input_text)

        file = open(output_file, "w")
        file.write(output_text)
        file.close()
    else:
        print("expected -c|-d")
        sys.exit()
