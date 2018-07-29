import os



def read_text_file(file_path):
    with open(file_path) as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result


def extract_float_from_str(in_str):
    float_str = ''
    for char in in_str:
        if char.isdigit() or char == '.':
            float_str += char
    return float(float_str)



def sec_to_min(sec):
    return sec / 60


def meters_to_miles(meters):
    return meters * 0.000621371



def file_names_in_dir(dir_path, file_ext):
    file_name_list = []
    for file in os.listdir(dir_path):
        if file.endswith(file_ext):
            file_name_list.append(file)
    return file_name_list




















import graph_data
if __name__ == '__main__':
    graph_data.main()   