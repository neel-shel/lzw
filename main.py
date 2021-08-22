import sys
from os import path
from lzw-compression import compress
from lzw-decompression import decompress

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

    file = open(input_file, "r")
    input_text = file.read()
    file.close()
        
    if option == '-c': #compress
        output_text = compress(input_text)
    else if option == '-d': #decompress
        pass
    else:
        print("expected -c|-d")
        sys.exit()

    print(output_text)

    file = open(output_file, "w")
    file.write(output_text)
    file.close()
