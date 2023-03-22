def get_puzzle_input(filename, as_int=False, as_list=False, remove_spaces=False):
    f = open(filename)
    input_array = f.readlines()
    f.close()
    output_array = []
    for line in input_array:
        if line.endswith('\n'):
            line = line.replace('\n', '')
        if remove_spaces:
            line = line.replace(' ', '')
        if as_int:
            if line.isnumeric():
                line = int(line)
            else:
                raise TypeError('Unable to convert line "'+line+'" into an integer')
        if as_list:
            line_list = []
            for value in line:
                line_list.append(value)
            output_array.append(line_list)
        else:
            output_array.append(line)
    return output_array
