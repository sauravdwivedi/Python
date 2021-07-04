"""Given a table of shoe sizes and names of people with these sizes:

42 42 43 45 42
Saurav Joe Albert Pepe Saurav

Write a script that:

1. Returns modal shoe size
2. In case there is no unique modal size, return "-1"
3. Returns name of modal names associated to modal size
4. In case of no modal size, return ""."""

import statistics as st

def shoe_size(sizes, names):
    """Method to find out modal size and modal name for modal size"""
    mode_sz = st.mode(sizes)
    index_of_modes = [i for i in range(len(sizes)) if sizes[i] == mode_sz]
    modal_names = [names[index_of_modes[i]] for i in range(len(index_of_modes))]
    mode_modal_names = st.mode(modal_names)
    index_of_modalname = [i for i in range(len(modal_names)) if modal_names[i] == mode_modal_names]
    x = 0
    y = ""
    if len(index_of_modes) > 1:
        x = mode_sz
    else:
        x = -1
    if len(index_of_modalname) > 1:
        y = mode_modal_names
    else:
        y = ""
    result = f"Modal shoe size is {x} and modal name for this size is '{y}'"
    return result
    
if __name__ == '__main__':
    input_file = 'ShoeSizes_input.txt'
    try:
        with open(input_file) as f:
            lines = f.read()
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    else:
        sizes = list(map(int, lines.split("\n")[0].split(" ")))
        names = lines.split("\n")[1].split(" ")
        result = shoe_size(sizes, names)
        print(result)
