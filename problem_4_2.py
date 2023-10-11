from TMparser import parseInput, printTM

"""
TO EXECUTE THE PROGRAM:
    cat "4.2.ptm " | python problem_4_2.py
"""

ZERO = "0"
ONE = "1"
UNDERLINE = "_"
STAR = "*"
SUBSTITUTE_LETTER = "Z"

"""
checkifExists: a function to check whether a rule has already been written
@params: lines -> rules already created, start_state -> start of rule, input -> letter of rule
@ returns boolean: if already created
"""
def checkifExists(lines, start_state, input):
    for line in lines:
        if start_state == line[0] and input == line[1]:
            return False
    return True


def go_to_furthest(num:str, direction:str, final_state:str, output_letter:str):
    if (direction == "L" or direction == 'l'):
        new_direction = "R"
    else:
        new_direction = "L"
    final_lines = []
    to_go = [num, "_", "_", new_direction, num+"a"]
    to_end = [[num+"a", "0", "0", new_direction, num+"a"],
              [num+"a", "1", "1", new_direction, num+"a"],
              [num+"a", "2", "2", new_direction, num+"a"],
              [num+"a", "3", "3", new_direction, num+"a"],
              [num+"a", SUBSTITUTE_LETTER, SUBSTITUTE_LETTER, new_direction, num+"a"],]
    actual_end = [num+"a", "_", "_", direction, num+"b"]
    find_new_zero = get_to_a_zero(num+"b", direction, final_state, 1, output_letter)
    final_lines.append(to_go)
    for line in to_end:
        final_lines.append(line)
    for line in find_new_zero:
        final_lines.append(line)
    final_lines.append(actual_end)
    return final_lines

def get_to_a_zero(num:str, direction:str, final_state:str, depth:int, output_letter:str):
    final_lines = []
    find_one = [[num, "1", "1", direction, num], 
                [num, "2", "2", direction, num],
                [num, "3", "3", direction, num]]
    for line in find_one:
        final_lines.append(line)
    # final_lines.append([num, SUBSTITUTE_LETTER, SUBSTITUTE_LETTER, direction, num])
    if (depth == 0):
        gets_to_end = go_to_furthest(num, direction, final_state, output_letter)
        for line in gets_to_end:
            final_lines.append(line)
    else:
        final_lines.append([num, SUBSTITUTE_LETTER, output_letter, "*", final_state])
    final_lines.append([num, ZERO, ZERO, "*", final_state])
    return final_lines


if __name__ == '__main__':
    # read an TM via stdin. See parser.py for details on the returned object
    lines = parseInput()
    final_lines = []
    # Put your code here:
    counter = 10
    for line in lines:
        start_state, input_letter, output_letter, direction, output_state = line
        if output_letter == ZERO or output_letter == STAR and output_state != "halt-reject" and output_state != "halt-accept":
            # follow direction
            if output_letter == ZERO:            
                final_lines.append([start_state, input_letter, SUBSTITUTE_LETTER, direction, str(counter)])
                new_rules = get_to_a_zero(str(counter), direction, output_state, 0, output_letter)
                counter += 1
                for line in new_rules:
                    final_lines.append(line)
                
            
          #############  HAPPY ABOVE  ############  
            else:
                if checkifExists(final_lines, start_state, ZERO):
                    final_lines.append([start_state, ZERO, SUBSTITUTE_LETTER, direction, str(counter)])
                if checkifExists(final_lines, start_state, ONE):
                    final_lines.append([start_state, ONE, ONE, direction, output_state])
                if checkifExists(final_lines, start_state, UNDERLINE):
                    final_lines.append([start_state, UNDERLINE, output_letter, direction, output_state])
                if checkifExists(final_lines, start_state, SUBSTITUTE_LETTER):
                    final_lines.append([start_state, SUBSTITUTE_LETTER, SUBSTITUTE_LETTER, direction, str(counter)])
                new_rules = get_to_a_zero(str(counter), direction, output_state, 0, output_letter)
                counter += 1
                for line in new_rules:
                    final_lines.append(line)
        else:
            final_lines.append(line)

    printTM(final_lines)

#  2 1 0 R 3