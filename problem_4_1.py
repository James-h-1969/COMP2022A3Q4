from parser import parseTM, printTM

ZERO = "0"

def go_to_furthest(num:str, direction:str):
    if (direction == "L"):
        new_direction = "R"
    else:
        new_direction = "L"
    final_lines = []
    to_go = [num, "_", "_", new_direction, num+"a"]
    to_end = [[num+"a", "0", "0", new_direction, num+"a"],
              [num+"a", "1", "1", new_direction, num+"a"],
              [num+"a", "2", "2", new_direction, num+"a"],
              [num+"a", "3", "3", new_direction, num+"a"]]
    actual_end = [num+"a", "_", "_", direction, num+"b"]
    find_new_zero = get_to_a_zero(num+"b", direction, "-1")
    final_lines.append(to_go)
    append1 = [final_lines.append(end) for end in to_end]
    final_lines.append(actual_end)
    append2 = [final_lines.append(final) for final in find_new_zero]
    return final_lines

def get_to_a_zero(num:str, direction:str, final_state:str):
    final_lines = []
    keep_moving = [[num, "1", "1", direction, num], 
                   [num, "2", "2", direction, num], 
                   [num, "3", "3", direction, num], ]
    if (final_state != -1):
        gets_to_end = go_to_furthest(num, direction)
        append2 = [final_lines.append(line) for line in gets_to_end]
    find_zero = [num, "0", "0", "*", final_state]
    final_lines.append(find_zero)
    append1 = [final_lines.append(line) for line in keep_moving]


if __name__ == '__main__':
    # read an TM via stdin. See parser.py for details on the returned object
    lines = parseTM()
    final_lines = []
    # Put your code here:
    counter = 10
    for line in lines:
        start_state, input_letter, output_letter, direction, output_state = line
        if input_letter == ZERO:
            # follow direction
            new_rules = get_to_a_zero(str(counter), direction, output_state)
            counter += 1
        else:
            final_lines.append(line)


    # if you use the same data structure, you can use:
    printTM(lines)
