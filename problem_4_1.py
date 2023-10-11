from TMparser import parseInput, printTM

"""
cat "4.1.tm " | python problem_4_1.py
"""

ZERO = "0"
ONE = "1"
STAR = "*"
UNDERLINE = "_"
REPLACEMENT_LETTER = "Z"

def checkifExists(lines, start_state, input):
    for line in lines:
        if start_state == line[0] and input == line[1]:
            return False
    return True

if __name__ == '__main__':
    # read an TM via stdin. See parser.py for details on the returned object
    lines = parseInput()
    final_lines = []
    # Put your code here:
    counter = 10

    for line in lines:
        start_state, input_letter, output_letter, direction, output_state = line
        
        if output_letter == ZERO or output_letter == STAR:
            if output_letter == ZERO:
                final_lines.append([start_state, input_letter, REPLACEMENT_LETTER, direction, output_state])
            if output_letter == STAR:
                if input_letter == STAR:
                    if checkifExists(final_lines, start_state, ZERO):
                        final_lines.append([start_state, ZERO, REPLACEMENT_LETTER, direction, output_state])
                        final_lines.append([start_state, REPLACEMENT_LETTER, REPLACEMENT_LETTER, direction, output_state])
                    if checkifExists(final_lines, start_state, ONE):
                        final_lines.append([start_state, ONE, ONE, direction, output_state])
                if input_letter == ZERO:
                    final_lines.append([start_state, ZERO, REPLACEMENT_LETTER, direction, output_state])
                    final_lines.append([start_state, REPLACEMENT_LETTER, REPLACEMENT_LETTER, direction, output_state])
        else:
            final_lines.append(line)

        if input_letter == ZERO:
            if output_letter == ZERO:
                final_lines.append([start_state, REPLACEMENT_LETTER, REPLACEMENT_LETTER, direction, output_state])
            else:
                final_lines.append([start_state, REPLACEMENT_LETTER, output_letter, direction, output_state])

    
    # print("Initial TM:")
    # printTM(lines)
    # print(" ")
    # print("Final PTM:")
    printTM(final_lines)

    

