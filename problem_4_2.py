from TMparser import parseInput, printTM

"""
TO EXECUTE THE PROGRAM:
    cat "4.2.ptm " | python problem_4_2.py
"""

ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
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

"""
go_to_furthest: a function that gets the head to the other side of the string
@params: num: starting state, direction -> direction it was travelling in, final_state -> 
the end state, output_letter -> final letter
@ returns: lines to make this happen
"""
def go_to_furthest(num:str, direction:str, final_state:str, output_letter:str):
    # figure out the reverse direction
    if (direction == "L" or direction == 'l'):
        new_direction = "R"
    else:
        new_direction = "L"

    final_lines = []

    final_lines.append([num, UNDERLINE, UNDERLINE, new_direction, num+"a"]) # entry into state

    final_lines.append([num+"a", UNDERLINE, UNDERLINE, direction, num+"b"]) # exit of state

    final_lines.append([num+"a", STAR, STAR, new_direction, num+"a"]) # move in direction
    
    # find the next zero at the new end
    find_new_zero = get_to_a_zero(num+"b", direction, final_state, 1, output_letter)
    for line in find_new_zero:
        final_lines.append(line)
    
    return final_lines

"""
get_to_a_zero: function that moves until it finds a zero
@params: num -> initial state, direction -> direction it is moving, final_state -> where it 
ends up, depth: to stop recursively checking forever, output_letter -> as implied
@returns: lines to make this happen
"""
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

def main():
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

if __name__ == '__main__':
    main()