



def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result


def extract_float_from_str(in_str):
    print('extracting:  ' + in_str)#````````````````````````````````````````````````````````````
    float_str = ''
    for char in in_str:
        if char.isdigit() or char == '.':
#             print(char)#`````````````````````````````````````````````````````````````````````````
            float_str += char
    return float(float_str)











import graph_data
if __name__ == '__main__':
    graph_data.main()   